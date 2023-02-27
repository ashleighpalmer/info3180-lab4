from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename



class LoginForm(FlaskForm):
   file= username = StringField('Username', validators=[InputRequired()])
   file=password = PasswordField('Password', validators=[InputRequired()])



class UploadForm(FlaskForm):
    file = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Upload')

