from flask import render_template, request, redirect, url_for, flash
from . import inscripciones 
from models import db, Alumnos, Curso, Inscripcion
import forms
from models import Curso 

@inscripciones.route("/inscribir", methods=['GET', 'POST'])
def inscribir_alumno():
    
    lista_alumnos = Alumnos.query.all()
    lista_cursos = Curso.query.all()
    
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        curso_id = request.form.get('curso_id')
        
        
        alumno = Alumnos.query.get(alumno_id) 
        curso = Curso.query.get(curso_id) 
        
        if alumno and curso:
            try:
                
                curso.alumnos.append(alumno) 
                db.session.commit() 
                flash("Inscripción realizada con éxito")
                return redirect(url_for('inscripciones.inscribir_alumno'))
            except Exception as e:
                db.session.rollback()
                flash("El alumno ya está inscrito en este curso") 
                
    return render_template("inscripciones/inscribir.html", alumnos=lista_alumnos, cursos=lista_cursos)




# En inscripciones/routes.py
@inscripciones.route('/consultar')
def consultar_inscripciones():
    materias = Curso.query.all()
    return render_template("inscripciones/listado.html", materias=materias)