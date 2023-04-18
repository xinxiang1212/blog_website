from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    name = StringField('what is your name', validators=[DataRequired()])
    submit = SubmitField('submit')

class EditProfileForm(FlaskForm):
    name = StringField('Real Name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')