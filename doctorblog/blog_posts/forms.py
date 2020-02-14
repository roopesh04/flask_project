#blog_post/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class postform(FlaskForm):

    patient_name=StringField("Patient Name",validators=[DataRequired()])
    medicine=TextAreaField("Medicine name",validators=[DataRequired()])
    submit=SubmitField("Post the medicine")