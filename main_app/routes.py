from datetime import datetime as dt
from flask import current_app as app
from flask import Blueprint,render_template, url_for, redirect, make_response, request
from flask_login import current_user, login_required, logout_user
from main_app.forms import ContactForm, SignupForm, SignupNewForm, LoginForm

from .models import User, db

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

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

@app.route('/sign-in', methods=["GET", "POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signin.html",
        form=form,
        time="Login Form")

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
            bio="In West Philadelphia born and raised, \ on the playground is where I spent most of my days",
            admin=False,
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for("user_records"))
    return render_template("users.jinja2", users=User.query.all(), title="Show Users")

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))