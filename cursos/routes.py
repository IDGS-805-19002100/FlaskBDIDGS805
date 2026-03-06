# cursos/routes.py
from flask import render_template, request, redirect, url_for
from . import cursos
from models import db, Curso, Maestros
from forms import CursoForm

@cursos.route("/registrocurso", methods=['GET', 'POST'])
def registro_curso():
    form = CursoForm()
    
   
    maestros_disponibles = Maestros.query.all()
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros_disponibles]
    
    if request.method == 'POST' and form.validate():
        nuevo_curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        
        return redirect(url_for('index')) 
    
    return render_template("cursos/registrocurso.html", form=form)





@cursos.route("/listado")
def lista_cursos():
    todos_los_cursos = Curso.query.all()
    
    return render_template("cursos/listacursos.html", cursos=todos_los_cursos)



@cursos.route("/detalles/<int:id>")
def detalles_curso(id):
    
    curso_obj = Curso.query.get_or_404(id)
    return render_template("cursos/detalles.html", curso=curso_obj)