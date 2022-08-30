from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Equalto, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.get(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username Already exists! Please try a different username.')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.get(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email address.')

    username = StringField(label='User Name:' validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address:' validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:' validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:' validators=[Equalto('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User name', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')