from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, TextAreaField, PasswordField, DateField, SelectField, SubmitField, validators)
from wtforms.fields.html5 import EmailField


class SignupForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField(
        'Email',
        [
            validators.Email(message='Not a valid email address.'),
            validators.DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        [
            validators.DataRequired(message="Please enter a password."),
        ]
    )
    confirmPassword = PasswordField(
        'Repeat Password',
        [
            validators.EqualTo('password', message='Passwords must match.')
        ]
    )
    title = SelectField(
        'Title',
        [validators.DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )
    website = StringField(
        'Website',
        validators=[validators.URL()]
    )
    birthday = DateField('Your Birthday')
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class SignupNewForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[validators.DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            validators.Length(min=6),
            validators.Email(message='Enter a valid email.'),
            validators.DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            validators.DataRequired(),
            validators.Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            validators.DataRequired(),
            validators.EqualTo('password', message='Passwords must match.')
        ]
    )
    website = StringField(
        'Website',
        validators=[validators.Optional()]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            validators.DataRequired(),
            validators.Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('Log In')


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
    body = TextAreaField(
        'Message',
        [
            validators.DataRequired(),
            validators.Length(min=4, message=('Your message is too short.'))
        ]
    )
    submit = SubmitField('Submit')
