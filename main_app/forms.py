from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, validators
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [validators.DataRequired()]
    )
    email = EmailField(
        'Email',
        [
            validators.Email(message=('Not a valid email address.')),
            validators.DataRequired()
        ]
    )
    body = TextField(
        'Message',
        [
            validators.DataRequired(),
            validators.Length(min=4, message=('Your message is too short.'))
        ]
    )
    recaptcha = RecaptchaField()
