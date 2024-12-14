from utils.db_util import execute_query, fetch_query_result
from utils.db_connection import db_connection

def test_insert_user(db_connection):
    """Test case to verify that a user is inserted into the database."""

    # Data to insert
    user_name = "Khan"
    user_email = "Khan@gamil.com"

    # Insert data into the database
    insert_query = """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
    """
    execute_query(db_connection, insert_query, (user_name, user_email))

    # Verify that the data was inserted
    select_query = "SELECT * FROM users WHERE email = %s"
    result = fetch_query_result(db_connection, select_query, (user_email,))

    assert len(result) == 1, "User was not inserted into the database."
    assert result[0][1] == user_name, f"Expected name '{user_name}', but got '{result[0][1]}'."
    assert result[0][2] == user_email, f"Expected email '{user_email}', but got '{result[0][2]}'."

    # Cleanup: Delete the test user
    delete_query = "DELETE FROM users WHERE email = %s"
    execute_query(db_connection, delete_query, (user_email,))
