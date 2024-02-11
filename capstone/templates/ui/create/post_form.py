from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired, Length

class PostForm(FlaskForm):
    post = StringField('Title', validators=[InputRequired(), Length(min=10, max=100)])
