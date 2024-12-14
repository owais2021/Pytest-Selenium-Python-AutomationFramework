import pytest
from utils.db_util import get_db_connection, close_db_connection

@pytest.fixture(scope="function")
def db_connection():
    """Fixture to set up and tear down the PostgreSQL connection."""
    conn = get_db_connection()
    yield conn  # Provide the connection to the test case
    close_db_connection(conn)  # Ensure the connection is closed after the test
