from flask import Blueprint

from services.services import create_user

# app= Blueprint('rutas', __name__)
main_blueprint = Blueprint('todo', __name__)

# Registrar rutas en el Blueprint
# @main_blueprint.route('/')

@main_blueprint.route('/', methods=['GET'])
def get_users():
    return 'Get all todos'


@main_blueprint.route('/<id>', methods=['GET'])
def get_user(id):
    return 'Get todo by id'

# Ruta  para crear 
@main_blueprint.route('/', methods=['POST'])
def get_create(): 
    # return 'Get todo by id'
    return create_user()

# Ruta para actualizar
@main_blueprint.route('/<id>', methods=['PUT'])
def update_todo(id):
    return 'Update todo'


# Ruta para eleminar
@main_blueprint.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    return 'Delete todo'

