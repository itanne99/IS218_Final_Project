from datetime import datetime as dt

from flask import current_app as app
from flask import render_template, url_for, redirect, make_response, request
from main_app.forms import ContactForm, SignupForm

from .models import User, db


@app.route('/')
def hello_world():
    return render_template('index.html', title="Hello world!")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        title="contact form"
    )


@app.route('/sign-up', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.html",
        form=form,
        time="Sign-up Form"
    )


@app.route('/success')
def success():
    return render_template('success.html', title="success")

@app.route('/users', methods=["GET"])
def getuser():
    """Create a user via query string parameters."""
    username = request.args.get("user")
    email = request.args.get("email")
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(f"{username} ({email}) already created!")
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
                on the playground is where I spent most of my days",
            admin=False,
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for("user_records"))
    return render_template("users.jinja2", users=User.query.all(), title="Show Users")
