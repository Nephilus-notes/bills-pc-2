from flask import Blueprint

bp = Blueprint('search', __name__, url_prefix='/pokemon/search')

from . import routes

