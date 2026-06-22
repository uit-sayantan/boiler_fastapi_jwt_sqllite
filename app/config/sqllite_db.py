import sqlite3

def get_conn():
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('my_database.db')
    return conn

def init_db():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        ip = input("Press Type 'Initialize' to Initialize the Empty Database: ")
        script_path = "ddl.sql"  # Path to your SQL script
        ip="Initialize"
        if ip.__eq__("Initialize"):
            print(f"Reading script: {script_path}...")
            with open(script_path, "r", encoding="utf-8") as sql_file:
                sql_script = sql_file.read()
            # Create the audit table if it doesn't exist
            cursor.executescript(sql_script)
            print("Database initialized successfully.")
        else:
            print("Database initialization skipped.")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

#init_db()