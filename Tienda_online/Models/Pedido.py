import uuid
from datetime import datetime
from Models.Usuario import Cliente
from Models.Producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente, items: list[tuple[Producto, int]]):
        self.cliente: Cliente = cliente
        self.id = str(uuid.uuid4().hex)
        self.fecha = datetime.now()
        self.items: list[tuple[Producto, int]] = items 
        self.numero_productos = sum(cantidad for _, cantidad in items)
    def __str__(self):
        return f"Pedido ID: {self.id}, Cliente: {self.cliente.nombre}, Productos: [{self.items}], Fecha: {self.fecha}, Número de productos: {self.numero_productos}"