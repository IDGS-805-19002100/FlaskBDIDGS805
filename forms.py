from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, EmailField
from wtforms import validators

class UserForm(Form):

    id = IntegerField('id')
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingrese nombre valido")
    ])
    
    apaterno = StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    email = EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])