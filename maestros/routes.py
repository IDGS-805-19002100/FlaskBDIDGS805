from flask import render_template, request, redirect, url_for
from . import maestros
import forms
from models import db, Maestros


@maestros.route("/maestros", methods=['GET', 'POST'])
def registro_maestro():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST' and create_form.validate():
        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    
    return render_template("maestros/Maestros.html", form=create_form)


@maestros.route("/lista_maestros", methods=['GET'])
def lista_maestros():
    resultado_maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", maestros=resultado_maestros)


@maestros.route("/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    mae = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    return render_template('maestros/detallesm.html', 
                         nombre=mae.nombre, 
                         apaterno=mae.apellidos, 
                         email=mae.email, 
                         especialidad=mae.especialidad)

@maestros.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    mae = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    
    
    create_form = forms.UserForm2(request.form, obj=mae)
    
    if request.method == 'GET':
        
        create_form.id.data = mae.matricula
        
        create_form.id.render_kw = {'readonly': True}
        create_form.nombre.render_kw = {'readonly': True}

    if request.method == 'POST':
        db.session.delete(mae)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    
    return render_template("maestros/eliminarm.html", form=create_form)








@maestros.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id = request.args.get('id')
   
    mae = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    
   
    create_form = forms.UserForm2(request.form, obj=mae)

    if request.method == 'POST' and create_form.validate():
        
        mae.nombre = create_form.nombre.data
        mae.apellidos = create_form.apellidos.data
        mae.especialidad = create_form.especialidad.data
        mae.email = create_form.email.data
        
        
        db.session.add(mae)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    
    return render_template("maestros/modificarm.html", form=create_form)