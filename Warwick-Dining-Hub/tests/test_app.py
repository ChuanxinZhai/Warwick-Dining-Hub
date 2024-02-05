import pytest
from flask_testing import TestCase
from app import app, get_db_connection, init_db

class MyTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True

    def create_app(self):
        # Flask-Testing requires this method to be implemented. It is used to create the Flask application.
        app.config['TESTING'] = True
        app.config['DATABASE'] = self.SQLALCHEMY_DATABASE_URI
        return app

    def setUp(self):
        # Setup that is run before every test.
        with app.app_context():
            init_db()  # Initialize the in-memory SQLite database.

    def tearDown(self):
        # Cleanup that is run after every test.
        with app.app_context():
            db = get_db_connection()
            db.close()

    def test_home_page(self):
        # Test the home page route.
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')

    def test_search(self):
        # Test the search functionality.
        response = self.client.get('/search?q=coffee')
        self.assert200(response)
        self.assertIn('coffee', response.data.decode('utf-8'))




# Write more tests as needed to cover other functionalities.

if __name__ == '__main__':
    pytest.main()
