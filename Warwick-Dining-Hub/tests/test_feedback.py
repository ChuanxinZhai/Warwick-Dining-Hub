import pytest
import os
import time
from feedback import get_db_connection, init_db, add_feedback, set_database_path

# Temporary database for testing
TEST_DB = 'test_feedback_hub.db'

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

def test_add_feedback(db):
    # Test adding feedback
    name = 'Test Name'
    email = 'test.email@example.com'
    restaurant = 'Test Restaurant'
    rating = 5
    message = 'Test message'

    add_feedback(name, email, restaurant, rating, message)

    # Query to verify the feedback was added
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM feedback WHERE email = ?", (email,))
        feedback = cur.fetchone()

        assert feedback is not None
        assert feedback['name'] == name
        assert feedback['email'] == email
        assert feedback['restaurant'] == restaurant
        assert feedback['rating'] == rating
        assert feedback['message'] == message
