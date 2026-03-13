from flask import Blueprint, render_template, request, session, flash
from models import db, Cliente, Pedido, DetallePedido
# Aquí importarías tu formulario de Flask-WTF

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/registrar', methods=['GET', 'POST'])
def registrar():
    # Lógica para manejar el botón "Agregar" y guardar en session['carrito']
    return render_template('pedidos/registro.html')