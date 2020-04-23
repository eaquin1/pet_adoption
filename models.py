from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://cdn1.vectorstock.com/i/1000x1000/08/65/cute-labrador-retriever-dog-avatar-vector-20670865.jpg"
db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def img_url(self):
        """Return image for pet"""
        return self.photo_url or GENERIC_IMAGE