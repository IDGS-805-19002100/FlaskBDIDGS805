from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectMultipleField, DateField, validators, widgets
from datetime import date

# Clase para permitir Checkboxes múltiples en los ingredientes
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PizzaForm(FlaskForm):
    # --- Datos del Cliente ---
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es obligatorio"),
        validators.Length(min=4, max=100)
    ])
    
    direccion = StringField("Dirección", [
        validators.DataRequired(message="La dirección es obligatoria")
    ])
    
    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El teléfono es obligatorio")
    ])

    fecha = DateField("Fecha de Compra", default=date.today, validators=[
        validators.DataRequired(message="Seleccione una fecha válida")
    ])

    # --- Detalles de la Pizza ---
    tamano = RadioField('Tamaño de Pizza', choices=[
        ('Chica', 'Chica $40'),
        ('Mediana', 'Mediana $80'),
        ('Grande', 'Grande $120')
    ], validators=[validators.DataRequired(message="Seleccione un tamaño")])

    ingredientes = MultiCheckboxField('Ingredientes ($10 c/u)', choices=[
        ('Jamon', 'Jamón'),
        ('Pina', 'Piña'),
        ('Champiñones', 'Champiñones')
    ])

    num_pizzas = IntegerField("Número de Pizzas", [
        validators.DataRequired(message="Ingrese al menos una pizza"),
        validators.NumberRange(min=1, message="Mínimo debe ser 1")
    ], default=1)

# Formulario para las consultas de ventas (Día/Mes)
class ConsultaVentasForm(FlaskForm):
    # Para la consulta por día de la semana (Lunes, Martes...)
    dia_semana = StringField("Día de la semana", [validators.Optional()])
    
    # Para la consulta por nombre de Mes
    mes = StringField("Mes", [validators.Optional()])