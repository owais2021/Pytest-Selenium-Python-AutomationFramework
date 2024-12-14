import psycopg2
from resources.db_config import DB_CONFIG

def get_db_connection():
    """Establish a database connection."""
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

def close_db_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()

def execute_query(conn, query, params=None):
    """Execute a query."""
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()

def fetch_query_result(conn, query, params=None):
    """Fetch the result of a SELECT query."""
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()
