from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, EmailField
from wtforms import validators

class UserForm(Form):

    id = IntegerField('id')
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingrese nombre valido")
    ])
    
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido")
    ])
    telefono = StringField("Telefono", [
        validators.DataRequired(message="Ingresa telefono valido")
    ])
    
    email = EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])