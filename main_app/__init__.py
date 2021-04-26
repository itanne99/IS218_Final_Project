from flask import Flask, render_template, url_for, redirect
from main_app.forms import ContactForm

app = Flask(__name__)


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
        form=form
    )


if __name__ == '__main__':
    app.run()
