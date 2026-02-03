# Database Schema

Banco de dados PostgreSQL hospedado no Supabase.

## Diagrama de Relacionamentos

```
┌─────────────┐       ┌─────────────────┐       ┌─────────────┐
│   series    │───────│  series_actors  │───────│   actors    │
└─────────────┘       └─────────────────┘       └─────────────┘
      │                                               │
      │               ┌─────────────────┐             │
      └───────────────│   series_tag    │             │
      │               └─────────────────┘             │
      │                       │                       │
      │               ┌─────────────────┐             │
      │               │      tags       │             │
      │               └─────────────────┘             │
      │                                               │
      │               ┌─────────────────┐             │
      └───────────────│   characters    │─────────────┘
                      └─────────────────┘
                              │
                      ┌───────┴───────┐
                      │               │
        ┌─────────────────────┐  ┌─────────────────────┐
        │   ship_characters   │  │    ship_actors      │
        └─────────────────────┘  └─────────────────────┘
                │                         │
┌───────────────────────────┐  ┌─────────────────────────┐
│ ship_characters_characters│  │   ship_actors_actors    │
└───────────────────────────┘  └─────────────────────────┘
                               │
                      ┌─────────────────────┐
                      │  ship_actors_series │
                      └─────────────────────┘
```

## Tabelas Principais

### series
Armazena as séries BL.

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| title | VARCHAR | Título da série |
| country | VARCHAR | País de origem |
| release_date | DATE | Data de lançamento |
| episode_number | INTEGER | Número de episódios |
| genre | VARCHAR | Gênero |
| synopsis | TEXT | Sinopse |
| platform | VARCHAR | Plataforma de streaming |
| rate | INTEGER | Nota (1-10) |
| status | VARCHAR | Status (Completed/Dropped) |
| production_company | VARCHAR | Produtora |
| date_start | DATE | Data que começou a assistir |
| date_watched | DATE | Data que terminou de assistir |

### actors
Armazena os atores.

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| nickname | VARCHAR | Apelido (único) |
| name | VARCHAR | Nome completo |
| birthday | DATE | Data de nascimento |
| nationality | VARCHAR | Nacionalidade |
| gender | VARCHAR | Gênero |
| agency | VARCHAR | Agência |
| ig | VARCHAR | Instagram |

### characters
Armazena os personagens das séries.

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| name | VARCHAR | Nome do personagem |
| series_id | INTEGER | FK → series.id |
| actor_id | INTEGER | FK → actors.id |
| role_type | VARCHAR | Tipo (main/support) |

### tags
Tags para categorizar séries.

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| name | VARCHAR | Nome da tag (único) |

### ship_actors
Ships de atores (casais reais).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| name | VARCHAR | Nome do ship |

### ship_characters
Ships de personagens (casais fictícios).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | PK, auto-increment |
| name | VARCHAR | Nome do ship |

## Tabelas de Associação (Junction Tables)

### series_actors
Relaciona séries com atores (N:N).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| series_id | INTEGER | FK → series.id |
| actor_id | INTEGER | FK → actors.id |

PK composta: (series_id, actor_id)

### series_tag
Relaciona séries com tags (N:N).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| series_id | INTEGER | FK → series.id |
| tag_id | INTEGER | FK → tags.id |

PK composta: (series_id, tag_id)

### ship_actors_actors
Relaciona ships com seus atores (N:N).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ship_id | INTEGER | FK → ship_actors.id |
| actor_id | INTEGER | FK → actors.id |

PK composta: (ship_id, actor_id)

### ship_actors_series
Relaciona ships de atores com séries (N:N).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ship_id | INTEGER | FK → ship_actors.id |
| series_id | INTEGER | FK → series.id |

PK composta: (ship_id, series_id)

### ship_characters_characters
Relaciona ships com seus personagens (N:N).

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ship_id | INTEGER | FK → ship_characters.id |
| character_id | INTEGER | FK → characters.id |

PK composta: (ship_id, character_id)

## Cascade Deletes

As foreign keys estão configuradas com `ON DELETE CASCADE`:
- Deletar uma série remove automaticamente seus relacionamentos em `series_actors`, `series_tag`, e `characters`
- Deletar um ator remove seus relacionamentos em `series_actors` e `ship_actors_actors`
- Deletar um personagem remove seus relacionamentos em `ship_characters_characters`

## Sincronização de Sequences

Se houver erro de "duplicate key" ao inserir, execute no Supabase:

```sql
SELECT setval('series_id_seq', (SELECT COALESCE(MAX(id), 0) FROM series));
SELECT setval('actors_id_seq', (SELECT COALESCE(MAX(id), 0) FROM actors));
SELECT setval('characters_id_seq', (SELECT COALESCE(MAX(id), 0) FROM characters));
SELECT setval('tags_id_seq', (SELECT COALESCE(MAX(id), 0) FROM tags));
SELECT setval('ship_actors_id_seq', (SELECT COALESCE(MAX(id), 0) FROM ship_actors));
SELECT setval('ship_characters_id_seq', (SELECT COALESCE(MAX(id), 0) FROM ship_characters));
```
