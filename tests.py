from unittest import TestCase

from app import app
from models import Pet, db

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_forms_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Don't req CSRF for testing
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class PetViewsTestCase(TestCase):
    """Tests for views for Pets"""

    def test_pet_add_form(self):
        with app.test_client() as client:
            resp = client.get("/new")
            html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<form method="POST">', html)
    
    def test_pet_add(self):
        with app.test_client() as client:
            d = {"name": "Doggie", "species": "dog", "age": 2, "notes": "test case cute"}
            resp = client.post("/new", data = d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h5 class="card-title">Doggie</h5>', html)
    
    def test_age_range(self):
        with app.test_client() as client:
            d = {"name": "Snoopie", "species": "snake", "age": 35}
            resp = client.post("/new", data = d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Number must be between 0 and 30.", html)