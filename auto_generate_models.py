"""
Gera automaticamente os models SQLAlchemy a partir do banco de dados
e substitui os arquivos existentes em app/models/
"""
import psycopg
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

# Mapeamento de tipos PostgreSQL para SQLAlchemy
TYPE_MAP = {
    'integer': 'Integer',
    'bigint': 'BigInteger',
    'character varying': 'String',
    'text': 'Text',
    'boolean': 'Boolean',
    'date': 'Date',
    'timestamp without time zone': 'DateTime',
    'numeric': 'Numeric',
    'real': 'Float',
    'double precision': 'Float',
}

def get_table_info(table_name):
    """Retorna informações completas sobre uma tabela"""
    # Colunas
    cur.execute(f"""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position
    """)
    columns = cur.fetchall()

    # Primary keys
    cur.execute(f"""
        SELECT a.attname
        FROM pg_index i
        JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        WHERE i.indrelid = '{table_name}'::regclass AND i.indisprimary
    """)
    pk_columns = [row[0] for row in cur.fetchall()]

    # Foreign keys
    cur.execute(f"""
        SELECT kcu.column_name, ccu.table_name, ccu.column_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = '{table_name}'
    """)
    fk_columns = {row[0]: (row[1], row[2]) for row in cur.fetchall()}

    # Unique constraints
    cur.execute(f"""
        SELECT a.attname
        FROM pg_index i
        JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        WHERE i.indrelid = '{table_name}'::regclass AND i.indisunique AND NOT i.indisprimary
    """)
    unique_columns = [row[0] for row in cur.fetchall()]

    return columns, pk_columns, fk_columns, unique_columns

def generate_model_code(table_name, class_name):
    """Gera o código Python do model para uma tabela"""
    columns, pk_columns, fk_columns, unique_columns = get_table_info(table_name)

    # Imports necessários
    imports = ["from sqlalchemy import Column, Integer, String"]
    used_types = set()

    # Determina quais tipos são necessários
    for col_name, data_type, is_nullable, default in columns:
        sa_type = TYPE_MAP.get(data_type, 'String')
        used_types.add(sa_type)

    # Adiciona tipos especiais aos imports
    special_types = used_types - {'Integer', 'String'}
    if special_types:
        imports[0] = f"from sqlalchemy import Column, Integer, String, {', '.join(sorted(special_types))}"

    if fk_columns:
        imports[0] += ", ForeignKey"

    imports.append("from app.models.base import Base")

    # Inicia o código do model
    lines = []
    lines.extend(imports)
    lines.append("")
    lines.append(f"class {class_name}(Base):")
    lines.append(f'    __tablename__ = "{table_name}"')
    lines.append("")

    # Adiciona colunas
    for col_name, data_type, is_nullable, default in columns:
        sa_type = TYPE_MAP.get(data_type, 'String')
        is_pk = col_name in pk_columns
        is_fk = col_name in fk_columns
        is_unique = col_name in unique_columns
        nullable = is_nullable == 'YES'

        # Monta a definição da coluna
        col_parts = [sa_type]

        if is_fk:
            fk_table, fk_column = fk_columns[col_name]
            col_parts.insert(0, f'ForeignKey("{fk_table}.{fk_column}")')

        col_def = f"Column({', '.join(col_parts)}"

        # Adiciona constraints
        if is_pk:
            col_def += ", primary_key=True"
        if not nullable and not is_pk:
            col_def += ", nullable=False"
        if is_unique:
            col_def += ", unique=True"

        col_def += ")"

        lines.append(f"    {col_name} = {col_def}")

    return "\n".join(lines)

# Tabelas principais (não são tabelas de associação)
main_tables = {
    'actors': 'Actor',
    'characters': 'Character',
    'series': 'Series',
    'tags': 'Tag',
    'ship_actors': 'ShipActor',
    'ship_characters': 'ShipCharacter',
}

# Tabelas de associação
association_tables = {
    'series_actors': 'SeriesActor',
    'series_tag': 'SeriesTag',
    'ship_actors_actors': 'ShipActorActor',
    'ship_actors_series': 'ShipActorSeries',
    'ship_characters_characters': 'ShipCharacterCharacter',
}

models_dir = Path("app/models")

print("Gerando models...\n")

# Gera models principais
for table_name, class_name in main_tables.items():
    code = generate_model_code(table_name, class_name)
    filename = models_dir / f"{table_name}.py"

    print(f"[OK] Gerando {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code + "\n")

# Gera models de associação
for table_name, class_name in association_tables.items():
    code = generate_model_code(table_name, class_name)
    filename = models_dir / f"{table_name}.py"

    print(f"[OK] Gerando {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code + "\n")

cur.close()
conn.close()

print("\n[SUCESSO] Models gerados com sucesso!")
print("\n[AVISO] Os relationships entre models precisam ser adicionados manualmente.")
print("        Os arquivos gerados contem apenas as colunas e foreign keys.")
