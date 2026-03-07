from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from config import DevelopmentConfig
from flask_migrate import Migrate
from maestros.routes import maestros
from alumnos.routes import alumnos
from curso.routes import curso

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(curso)
db.init_app(app)
migrate=Migrate(app,db)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

