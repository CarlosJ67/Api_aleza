from bson import ObjectId

class ProductosController:
    def __init__(self, collection):
        self.collection = collection

    def crear_producto(self, producto):
        result = self.collection.insert_one(producto)
        return str(result.inserted_id)

    def obtener_productos(self):
        productos = []
        for producto in self.collection.find():
            producto['_id'] = str(producto['_id'])
            productos.append(producto)
        return productos

    def obtener_producto(self, producto_id):
        producto = self.collection.find_one({"_id": ObjectId(producto_id)})
        if producto:
            producto['_id'] = str(producto['_id'])
        return producto

    def actualizar_producto(self, producto_id, nuevos_datos):
        result = self.collection.update_one({"_id": ObjectId(producto_id)}, {"$set": nuevos_datos})
        return result.modified_count

    def eliminar_producto(self, producto_id):
        result = self.collection.delete_one({"_id": ObjectId(producto_id)})
        return result.deleted_count