"""Adopt application."""

from flask import Flask, request, flash
from flask.templating import render_template
from werkzeug.utils import redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# the toolbar is only enabled in debug mode:
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'nerea'

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


########################################################################

@app.route("/")
def home():
    """Show homepage with list of pets"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Show/Handle form to add pets"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo = form.photo.data
        notes = form.notes.data
        flash(f"Added {name} a {species} of age {age}", "info")

        new_pet = Pet(
            name=name,
            species=species,
            age=age,
            photo_url=photo,
            notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("addPet.html", form=form)


@app.route("/pet/<pet_id>", methods=["GET", "POST"])
def show_pet(pet_id):
    """Show details for a specific pet"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        if form.available.data == 'no':
            pet.available = False
        else:
            pet.available = True
        pet.phot_url = form.photo.data
        pet.notes = form.notes.data

        db.session.commit()

        flash(f"{pet.name} updated successfully", "info")

        return redirect("/")

    else:
        return render_template("pet.html", pet=pet, form=form)


@app.route("/delete/<pet_id>", methods=["POST"])
def delete_pet(pet_id):
    """Delete a pet from the list and db"""

    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()

    flash(f"{pet.name} removed!", 'error')

    return redirect("/")
