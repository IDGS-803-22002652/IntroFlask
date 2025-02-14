from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField,EmailField
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange

IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=StringField('Matricula')
    edad=IntegerField('Edad')
    nombre=StringField('Nombre')
    apellidos=StringField('Apellidos')
    email=EmailField('Correo')
    