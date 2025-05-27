from bson import ObjectId
from pymongo.errors import PyMongoError

class ProductosController:
    def __init__(self, collection):
        self.collection = collection

    def crear_producto(self, producto):
        try:
            result = self.collection.insert_one(producto)
            return {"_id": str(result.inserted_id)}
        except PyMongoError as e:
            return {"error": str(e)}

    def obtener_productos(self):
        productos = []
        try:
            for producto in self.collection.find():
                producto['_id'] = str(producto['_id'])
                productos.append(producto)
            return productos
        except PyMongoError as e:
            return {"error": str(e)}

    def obtener_producto(self, producto_id):
        try:
            producto = self.collection.find_one({"_id": ObjectId(producto_id)})
            if producto:
                producto['_id'] = str(producto['_id'])
                return producto
            else:
                return None
        except PyMongoError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Invalid ID format: {e}"}

    def actualizar_producto(self, producto_id, nuevos_datos):
        try:
            result = self.collection.update_one({"_id": ObjectId(producto_id)}, {"$set": nuevos_datos})
            if result.matched_count == 0:
                return {"message": "Producto no encontrado"}
            return {"message": "Producto actualizado", "modified_count": result.modified_count}
        except PyMongoError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Invalid ID format: {e}"}

    def eliminar_producto(self, producto_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(producto_id)})
            if result.deleted_count == 0:
                return {"message": "Producto no encontrado"}
            return {"message": "Producto eliminado", "deleted_count": result.deleted_count}
        except PyMongoError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Invalid ID format: {e}"}
