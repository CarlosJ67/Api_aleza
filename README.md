# API Tienda de Productos

Esta es una API sencilla para gestionar productos en un centro comercial o tienda. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
api-tienda-productos
├── src
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── controllers
│   │   └── productos_controller.py # Controlador para manejar operaciones CRUD de productos
│   ├── models
│   │   └── producto.py          # Modelo que define la estructura de un producto
│   ├── routes
│   │   └── productos_routes.py   # Rutas de la API para productos
│   └── db
│       └── conexion.py          # Manejo de la conexión a la base de datos MongoDB
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto
```

## Requisitos

Para ejecutar esta API, asegúrate de tener instaladas las siguientes dependencias:

- Flask
- PyMongo

Puedes instalar las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Configuración

1. Asegúrate de tener MongoDB instalado y en funcionamiento.
2. Configura la conexión a la base de datos en `src/db/conexion.py` según tus credenciales de MongoDB.
3. Ejecuta la aplicación con el siguiente comando:

```
python src/main.py
```

La API estará disponible en `http://localhost:5000`.

## Endpoints

- `POST /productos`: Crear un nuevo producto.
- `GET /productos`: Obtener la lista de productos.
- `GET /productos/<id>`: Obtener un producto por su ID.
- `PUT /productos/<id>`: Actualizar un producto por su ID.
- `DELETE /productos/<id>`: Eliminar un producto por su ID.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.