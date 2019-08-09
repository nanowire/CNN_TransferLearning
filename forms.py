from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from flask_wtf.file import FileRequired, FileAllowed, FileField
from models import User

# citation for forms: The Flask Megatutorial and flask-wtf.readthedocs.io

# to create new users
class NewUsersForm(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), 
		EqualTo('password')])
	submit = SubmitField('Register')


# to enable existing user sign in 
class SignInForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Enter')


# form for file upload
class PhotoUploadForm(FlaskForm):
	upload_photo = FileField('image', validators=[FileRequired(), 
		FileAllowed(['png','jpeg', 'jpg'], 'JPEG Images, only!')])

		