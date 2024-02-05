import pytest
import os
import time
from add_inventory import get_db_connection, init_db, add_product, set_database_path

# Temporary database for testing
TEST_DB = 'test_inventory_hub.db'

@pytest.fixture(scope='module')
def db():
    # Setup: Create a temporary database
    set_database_path(TEST_DB)
    init_db()

    yield

    try:
        time.sleep(2) # Sleep to ensure the database is not in use
        os.remove(TEST_DB)
    except PermissionError as e:
        print(f"Unable to remove database file due to: {e}")

def test_add_new_product(db):
    # Test adding a new product
    name = 'Test Product'
    category = 'Test Category'
    price = 9.99
    size = '500ml'
    image = 'test_product.png'
    facility = 'Test Facility'

    add_product(name, category, price, size, image, facility)

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM product WHERE name = ? AND category = ?", (name, category))
        product = cur.fetchone()

        assert product is not None
        assert product['name'] == name
        assert product['category'] == category
        assert product['price'] == price
        assert product['size'] == size
        assert product['image'] == image
        assert product['facility'] == facility

def test_add_existing_product(db):
    # Test adding an existing product
    name = 'Americano'
    category = 'Coffee'
    price = 2.5
    size = '200ml'
    image = 'Americano.png'
    facility = 'StarBucks Cafe'

    add_product(name, category, price, size, image, facility)
    
    # Attempt to add the same product again
    add_product(name, category, price, size, image, facility)

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) AS count FROM product WHERE name = ? AND category = ?", (name, category))
        count = cur.fetchone()['count']

        # Verify that the product was not added again
        assert count == 1
