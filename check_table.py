from app.core.database import engine
from sqlalchemy import inspect

inspector = inspect(engine)

if 'ship_characters_series' in inspector.get_table_names():
    cols = inspector.get_columns('ship_characters_series')
    print('ship_characters_series columns:')
    for c in cols:
        print(f"  {c['name']}: {c['type']}")
else:
    print('Table ship_characters_series not found')
