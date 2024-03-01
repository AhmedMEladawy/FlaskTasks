from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired,length,Email,EqualTo

class LoginForm(FlaskForm):
    
    username=StringField('username',validators=[DataRequired(),length(max=10)])
    password=PasswordField('password',validators=[DataRequired(),length(min=9)])
    submit=SubmitField('submit')
    
    
class SignupForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),length(max=10)])
    email=EmailField('email',validators=[DataRequired(),Email()])
    password=StringField('password',validators=[DataRequired(),length(max=10)])
    confirm_password=StringField('confirm password',validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('submit')