from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField,EmailField,validators
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange

IntegerField, SelectField

class UserForm(Form):
    matricula=StringField("Matricula",[
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=2,max=10,message="La matricula debe tener 8 caracteres")])
    edad=IntegerField("Edad",[
        validators.DataRequired(message="Campo requerido")])
    nombre=StringField("Nombre",
        validators=[DataRequired(message="Campo requerido")])
    apellidos=StringField("Apellidos",
        validators=[DataRequired(message="Campo requerido")])
    email=EmailField("Correo",
        validators=[DataRequired(message="Campo requerido")])
    