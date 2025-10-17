class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def consultar_stock(self):
        return self.cantidad

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
    
    def actualiza_stock(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return f"Id: {self.id}, Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    

class ProductoElectronico(Producto):
    def __init__(self, id, nombre, precio, cantidad, garantia):
        super().__init__(id, nombre, precio, cantidad)
        self.garantia = garantia

    def __str__(self):
        return f"{super().__str__()}, Garantía: {self.garantia} meses"

class ProductoRopa(Producto):
    def __init__(self, id, nombre, precio, cantidad, talla, color):
        super().__init__(id, nombre, precio, cantidad)
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Talla: {self.talla}, Color: {self.color}"