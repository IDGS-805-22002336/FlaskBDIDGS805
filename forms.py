from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField
from wtforms import validators
from wtforms import EmailField
from wtforms.validators import DataRequired


class UserForm2(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    apellido=StringField("Apellido", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=170, message="Ingrese el valor valido")
    ])
    email = EmailField("correo", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Email(message="Ingrese un correo valido"),
    ])
    telefono = StringField("telefono", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Length(min=3, max=20,message="Ingrese un telefono valido"),
    ])
    
class UserForm(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=70, message="Ingrese el valor valido")
    ])
    apellido=StringField("Apellido", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=70, message="Ingrese el valor valido")
    ])
    especialidad = StringField("especialidad", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Length(min=3, max=70,message="Ingrese su especialidad valido"),
    ])
    email = EmailField("correo", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Email(message="Ingrese un correo valido"),
    ])
    
    
    
class UserCurso(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("nombre del curso", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=70, message="Ingrese el valor valido")
    ])
    descripcion=StringField("descripcion", [
        validators.DataRequired(message="el campo es reuqerido"),
        validators.Length(min=3, max=70, message="Ingrese el valor valido")
    ])
    maestro_id = StringField("Maestro ID", [
    validators.DataRequired(message="el campo es requerido"),
    validators.Length(min=3, max=70,message="Ingrese un valor valido"),
    ])