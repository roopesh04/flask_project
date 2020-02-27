#blog_post/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField
from wtforms.validators import DataRequired

class postform(FlaskForm):

    patient_name=StringField("Patient Name",validators=[DataRequired()])
    medicine=TextAreaField("Medicine name",validators=[DataRequired()])
    description=TextAreaField("Description of the problem",validators=[DataRequired()])
    allergy=TextAreaField("Allergy due to the problem",validators=[DataRequired()])
    morning=BooleanField("Does it required to take medicine on morning?")
    afternoon=BooleanField("Does it required to take medicine on afternoon?")
    evening=BooleanField("Does it required to take medicine on evening?")
    submit=SubmitField("Post the medicine")