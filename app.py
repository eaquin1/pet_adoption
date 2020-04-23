from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import EditPetForm, AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "shhhhh"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///pets_db"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def render_home():
    """Render home page with list of pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """Renders and handles the edit pet form"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
       form.populate_obj(pet)
       db.session.add(pet)
       db.session.commit()
       return redirect('/')
    else:
        return render_template("edit_pet.html", pet=pet, form=form)

@app.route('/new', methods=["GET", "POST"])
def new_pet():
    """Renders and handles the new pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("new_pet.html", form=form)