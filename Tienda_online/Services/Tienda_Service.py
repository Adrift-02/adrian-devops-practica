from Models.Producto import Producto
from Models.Usuario import Cliente, Administrador
from Models.Pedido import Pedido
class Tienda_Service:
    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.pedidos = []
    
    def comprobar_stock(self, Producto):
        return Producto.cantidad > 0
    
    def registrar_cliente(self, cliente: Cliente):
        self.usuarios.append(cliente)

    def registrar_administrador(self, administrador: Administrador):
        self.usuarios.append(administrador)

    def añadir_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto: Producto):
        self.productos.remove(producto)

    def listar_productos(self):
        return [str(p) for p in self.productos]

    def realizar_pedido(self, cliente: Cliente, productos: Producto, fecha):
        if all(self.comprobar_stock(p) for p in productos):
            return self.generar_pedido(cliente, productos, fecha)
        else:
            raise Exception("No hay suficiente stock para uno o más productos.")   
        
    def generar_pedido(self, cliente: Cliente, productos: Producto, id, fecha):
        pedido = Pedido(cliente, productos, id, fecha)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos(self):
        return [str(p) for p in self.pedidos]