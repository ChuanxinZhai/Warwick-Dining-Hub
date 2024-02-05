import pytest
import os
import time
from check_stock import get_db_connection, fetch_products, set_database_path

from add_inventory import init_db

# Temporary database for testing
TEST_DB = 'test_stock_hub.db'

@pytest.fixture(scope='module')
def db():
    # Setup: Create a temporary database
    set_database_path(TEST_DB)
    # Initialize the database structure and add some test products
    # (Consider creating a separate function to initialize test data)
    init_db()  

    yield

    try:
        time.sleep(2) # Sleep to ensure the database is not in use
        os.remove(TEST_DB)
    except PermissionError as e:
        print(f"Unable to remove database file due to: {e}")

def test_fetch_products(db):
    products = fetch_products()



