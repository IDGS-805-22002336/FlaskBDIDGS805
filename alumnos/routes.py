from flask import render_template, request, redirect, url_for
from . import alumnos
from models import db, Alumnos
import forms


@alumnos.route("/lista")
def lista():
    alumno = Alumnos.query.all()
    return render_template("alumnos/lista.html", alumno=alumno)

@alumnos.route("/alumnos", methods=['GET', 'POST'])
def lista_alumnos():
    create_form = forms.UserForm2(request.form)

    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellido=create_form.apellido.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.lista'))

    return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET', 'POST'])
def detallesAlum():
    id = request.args.get('id')

    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    return render_template(
        "alumnos/detalles.html",
        alumno=alum1
    )
    
@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificarAlum():
    create_form = forms.UserForm2(request.form)
    
    if request.method =='GET':
        id=request.args.get('id')
        ''' #select * from alumnos where id=id '''
        alum1=db.session.query(Alumnos).filter(Alumnos.id ==id).first()
        create_form.id.data=alum1.id
        create_form.nombre.data=alum1.nombre
        create_form.apellido.data=alum1.apellido
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono
        
    if request.method == 'POST':
        id=create_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellido=create_form.apellido.data
        alum1.email=create_form.email.data
        alum1.telefono=create_form.telefono.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.lista'))
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminarAlum():
    create_form = forms.UserForm2(request.form)
    if request.method =='GET':
        id=request.args.get('id')
        ''' #select * from alumnos where id=id '''
        alum1=db.session.query(Alumnos).filter(Alumnos.id ==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellido.data = alum1.apellido
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
        
    if request.method == 'POST':
        id=create_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id ==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellido=create_form.apellido.data
        alum1.email=create_form.email.data
        alum1.telefono=create_form.telefono.data
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.lista'))

    return render_template("alumnos/eliminar.html", form=create_form)
