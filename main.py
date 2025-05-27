from flask import Flask
import os
from src.db.conexion import get_db_connection
from src.routes.productos_routes import configurar_rutas

def crear_app():
    app = Flask(__name__)
    
    # Inicializar conexión a la base de datos
    get_db_connection()
    
    # Configurar rutas
    configurar_rutas(app)
    
    return app

if __name__ == "__main__":
    app = crear_app()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

