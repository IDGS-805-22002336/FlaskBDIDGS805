from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField
from wtforms import validators
from wtforms import EmailField


class UserForm2(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    email = EmailField("correo", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Email(message="Ingrese un correo valido"),
    ])
