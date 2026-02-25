from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from config import DevelopmentConfig
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app,db)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    create_form = forms.UserForm2()
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_form, alumno=alumno)


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
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
        return redirect(url_for('index'))

    return render_template("Alumnos.html", form=create_form)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    
    if request.method =='GET':
        id=request.args.get('id')
        ''' #select * from alumnos where id=id '''
        alum1=db.session.query(Alumnos).filter(Alumnos.id ==id).first()
        nombre=alum1.nombre
        apellido=alum1.apellido
        email=alum1.email
        telefono=alum1.telefono
        
    return render_template("detalles.html", id=id, nombre=nombre,
                            apellido=apellido, email=email, telefono=telefono)
    
@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
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
        return redirect(url_for('index'))
    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
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
        return redirect(url_for('index'))

    return render_template("eliminar.html", form=create_form)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
