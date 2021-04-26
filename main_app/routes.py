from flask import current_app as app
from flask import render_template, url_for, redirect
from main_app.forms import ContactForm, SignupForm


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
