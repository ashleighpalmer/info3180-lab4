from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash




class LoginForm(FlaskForm):
   username = StringField('Username', validators=[InputRequired()])
   password = PasswordField('Password', validators=[InputRequired()])
   submit = SubmitField('Sign In')


class UploadForm(FlaskForm):
    file = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Upload')

