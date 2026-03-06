from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, EmailField, TextAreaField, SelectField, validators # Se agregó SelectField aquí

# Formulario para Alumnos
class UserForm(FlaskForm): 
    id = IntegerField('id')
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingrese nombre valido")
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

# Formulario para Maestros
class UserForm2(FlaskForm):
    id = IntegerField('matricula')
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingrese nombre valido")
    ])
    
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="Ingresa una especialidad válida")
    ])
    
    email = EmailField("Email", [
        validators.Email(message="Ingresa correo valido")
    ])

# Formulario para Cursos (Relación Uno a Muchos con Maestros) [cite: 9]
class CursoForm(FlaskForm):
    nombre = StringField("Nombre del Curso", [
        validators.DataRequired(message="El nombre de la materia es obligatorio"),
        validators.Length(min=3, max=150) # El PDF indica máximo 150 caracteres para el curso 
    ])
    
    descripcion = TextAreaField("Descripción del Curso", [
        validators.DataRequired(message="Agregue una breve descripción")
    ])
    
    # Campo para seleccionar al maestro que imparte el curso [cite: 10, 27]
    maestro_id = SelectField("Maestro que imparte", coerce=int)