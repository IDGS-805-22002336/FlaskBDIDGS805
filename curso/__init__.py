from flask import Blueprint

curso = Blueprint(
    'curso',
    __name__,
    template_folder='templates'
)

from . import routes