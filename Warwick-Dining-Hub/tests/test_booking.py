import pytest
import sqlite3
import os
import time
from sqlite3 import Connection

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from booking import get_db_connection, init_db, add_booking, set_database_path



# Temporary database for testing
TEST_DB = 'test_dining_hub.db'

@pytest.fixture(scope='module')
def db():
    # Setup: Create a temporary database
    set_database_path(TEST_DB)
    init_db()

    yield 
    # Teardown: Remove the temporary database after tests are done
    try:
        time.sleep(2) # Sleep to ensure the database is not in use
        os.remove(TEST_DB)
    except PermissionError as e:
        print(f"Unable to remove database file due to: {e}")
      


def test_get_db_connection(db):
    conn = get_db_connection()
    assert isinstance(conn, Connection)
    conn.close()

def test_add_booking(db):
    # Example test for adding a booking
    name = 'Test Name'
    email = 'test@example.com'
    date = '2024-02-25'
    time = '12:00:00'
    guests = 3
    facility = 'Test Facility'

    # Add booking
    add_booking(name, email, date, time, guests, facility)

    # Query to verify the booking was added
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM booking WHERE name = ?", (name,))
        booking = cur.fetchone()
        
        assert booking is not None
        assert booking['name'] == name
        assert booking['email'] == email
        assert booking['date'] == date
        assert booking['time'] == time
        assert booking['guests'] == guests
        assert booking['facility'] == facility

