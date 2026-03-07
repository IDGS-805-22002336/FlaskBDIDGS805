import forms
from . import maestros
from flask import render_template, request, redirect, url_for
from models import db, Maestros


@maestros.route("/maestros", methods=['GET', 'POST'])
def listas_maestros():
    create_form = forms.UserForm(request.form)
    listas_maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=listas_maestros)

@maestros.route("/agregar", methods=['GET', 'POST'])
def agregarMaes():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST' and create_form.validate():
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellido=create_form.apellido.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.listas_maestros'))

    return render_template("maestros/Maestros.html", form=create_form)

@maestros.route("/detallesMaes", methods=['GET'])
def detallesMaes():

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        nombre = maes.nombre
        apellido = maes.apellido
        especialidad = maes.especialidad
        email = maes.email

    return render_template("maestros/detallesMaes.html", maes=maes)

@maestros.route("/modificar/<int:matricula>", methods=['GET','POST'])
def modificarMaes(matricula):

    maes = Maestros.query.get_or_404(matricula)
    form = forms.UserForm(obj=maes)

    if request.method == 'POST' and form.validate():
        maes.nombre = form.nombre.data
        maes.apellido = form.apellido.data
        maes.especialidad = form.especialidad.data
        maes.email = form.email.data

        db.session.commit()
        return redirect(url_for('maestros.listas_maestros'))

    return render_template("maestros/modificarMaes.html", form=form)


@maestros.route("/eliminarMaes", methods=['GET', 'POST'])
def eliminarMaes():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        matricula = request.args.get('matricula')

        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.id.data = maes.matricula
        create_form.nombre.data = maes.nombre
        create_form.apellido.data = maes.apellido
        create_form.especialidad.data = maes.especialidad
        create_form.email.data = maes.email

    if request.method == 'POST':
        matricula = create_form.id.data
        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        maes.nombre=create_form.nombre.data
        maes.apellido=create_form.apellido.data
        maes.especialidad=create_form.especialidad.data
        maes.email=create_form.email.data
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.listas_maestros'))

    return render_template("maestros/eliminarMaes.html", form=create_form)


'''@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"perfil de {nombre}"'''
    
