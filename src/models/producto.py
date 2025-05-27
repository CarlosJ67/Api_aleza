class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "cantidad": self.cantidad
        }