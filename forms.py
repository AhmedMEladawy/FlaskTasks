from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField
from wtforms.validators import DataRequired, length

class SignupForm(FlaskForm):
    fullname = StringField('Employee Name', validators=[DataRequired(), length(max=50)])
    age = IntegerField('Employee Age',validators=[DataRequired()])
    salary = IntegerField('Employee Salary',validators=[DataRequired()])
    department = StringField('Employee Dept', validators=[DataRequired(), length(max=10)])
    submit = SubmitField('Submit')