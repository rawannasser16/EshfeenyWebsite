from db import get_db, close_db

def create_tables():
    connect_db = get_db()
    try:
        
        with open('tables.sql', 'r') as sql:
            connect_db.executescript(sql.read())
    except Exception as err:
        print(str(err))    
    connect_db.commit()
    close_db(connect_db)

create_tables()