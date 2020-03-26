#blog_post/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField
from wtforms.validators import DataRequired

class postform(FlaskForm):

    patient_name=StringField("Patient Name",validators=[DataRequired()])
    medicine=TextAreaField("Medicine name",validators=[DataRequired()])
    description=TextAreaField("Description of the problem",validators=[DataRequired()])
    allergy=TextAreaField("Allergy due to the problem",validators=[DataRequired()])
    timing=TextAreaField("Timing in which the medecine should be taken",validators=[DataRequired()])
    submit=SubmitField("Post the medicine")