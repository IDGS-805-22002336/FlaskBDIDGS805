from flask import render_template, request, redirect, url_for
from . import curso
from models import db, Curso, Alumnos
import forms

@curso.route("/listaCur")
def listaC():
    cursos = Curso.query.all()
    return render_template("curso/listadoCur.html", cursos=cursos)

@curso.route("/curso", methods=['GET', 'POST'])
def lista_curso():
    create_form = forms.UserCurso(request.form)
    mensaje = None

    if request.method == 'POST' and create_form.validate():

        curso = Curso.query.filter_by(nombre=create_form.nombre.data).first()

        if curso:
            mensaje = "Ya existe un curso con ese nombre"
        else:
            cur = Curso(
                nombre=create_form.nombre.data,
                descripcion=create_form.descripcion.data,
                maestro_id=create_form.maestro_id.data
            )

            db.session.add(cur)
            db.session.commit()

            return redirect(url_for('curso.listaC'))

    return render_template("curso/cursos.html", form=create_form, mensaje=mensaje)


@curso.route("/inscribir/<int:curso_id>", methods=['POST'])
def inscribir(curso_id):

    alumno_id = request.form.get("alumno_id")

    if not alumno_id:
        return redirect(url_for('curso.detalleCur', id=curso_id))

    curso = Curso.query.get_or_404(curso_id)
    alumno = Alumnos.query.get_or_404(int(alumno_id))

    if alumno not in curso.alumnos:
        curso.alumnos.append(alumno)
        db.session.commit()

    return redirect(url_for('curso.detalleCur', id=curso_id))

@curso.route("/detalleCur/<int:id>")
def detalleCur(id):
    form = forms.UserCurso(request.form)
    curso = Curso.query.get_or_404(id)
    alumnos = Alumnos.query.all()

    return render_template(
        "curso/detallesCur.html",
        curso=curso,
        alumnos=alumnos,
        form=form
    )

@curso.route("/eliminarCur", methods=['GET', 'POST'])
def eliminarCur():
    create_form = forms.UserCurso(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        curso1 = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso1.id
        create_form.nombre.data = curso1.nombre
        create_form.descripcion.data = curso1.descripcion
        create_form.maestro_id.data = curso1.maestro_id

    if request.method == 'POST':
        id = create_form.id.data
        curso1 = db.session.query(Curso).filter(Curso.id == id).first()
        curso1.nombre=create_form.nombre.data
        curso1.descripcion=create_form.descripcion.data
        curso1.maestro_id=create_form.maestro_id.data
        db.session.delete(curso1)
        db.session.commit()
        return redirect(url_for('curso.listaC'))

    return render_template("curso/eliminarCur.html", form=create_form)

@curso.route("/modificarCur/<int:id>", methods=['GET','POST'])
def modificarCur(id):
    curso = Curso.query.get_or_404(id)
    form = forms.UserCurso(obj=curso)

    if request.method == 'POST' and form.validate():
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        
        db.session.commit()
        return redirect(url_for('curso.listaC'))

    return render_template("curso/modificarCur.html", form=form)