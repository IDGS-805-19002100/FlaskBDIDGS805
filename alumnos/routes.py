from flask import render_template, request, redirect, url_for
from . import alumnos
import forms
from models import db, Alumnos

@alumnos.route("/listado")
def listado_alumnos():
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/listadoalumnos.html", alumnos=alumnos_list)

@alumnos.route("/registro", methods=['GET', 'POST'])
def registro_alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            telefono=create_form.telefono.data,
            email=create_form.email.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.listado_alumnos'))
    return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    # Obtenemos el objeto completo del alumno
    alum = Alumnos.query.get_or_404(id)
    # Pasamos el objeto 'alum' a la plantilla
    return render_template('alumnos/detalles.html', alumno=alum)

@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id = request.args.get('id')
    alum = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm(request.form, obj=alum)

    if request.method == 'POST' and create_form.validate():
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('alumnos.listado_alumnos'))
    
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    alum = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm(request.form, obj=alum)
    
    if request.method == 'POST':
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.listado_alumnos'))
        
    return render_template("alumnos/eliminar.html", form=create_form)