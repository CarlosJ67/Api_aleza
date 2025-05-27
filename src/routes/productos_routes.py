from flask import Blueprint, request, jsonify
from src.controllers.productos_controller import ProductosController
from src.db.conexion import get_db_connection

coleccion, client = get_db_connection()
controller = ProductosController(coleccion)

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    producto = controller.crear_producto(data)
    return jsonify(producto), 201

@productos_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = controller.obtener_productos()
    return jsonify(productos), 200

@productos_bp.route('/productos/<string:id>', methods=['GET'])
def obtener_producto(id):
    producto = controller.obtener_producto(id)
    return jsonify(producto), 200

@productos_bp.route('/productos/<string:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    producto_actualizado = controller.actualizar_producto(id, data)
    return jsonify(producto_actualizado), 200

@productos_bp.route('/productos/<string:id>', methods=['DELETE'])
def eliminar_producto(id):
    controller.eliminar_producto(id)
    return jsonify({'message': 'Producto eliminado'}), 204

def configurar_rutas(app):
    app.register_blueprint(productos_bp)