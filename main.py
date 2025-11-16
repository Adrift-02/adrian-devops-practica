from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Cliente, Administrador
from Models.Pedido import Pedido

# Crear algunos productos
producto1 = ProductoElectronico("Portatil", 1000.0, 2, 30, 5)
producto2 = ProductoRopa("Sudadera", 20.0, 5, 2, 'M', "Rojo")
producto3 = Producto("Carcasa", 15.0, 10, 1)
producto3 = ProductoElectronico("Cargador", 25.0, 8, 1, 2)
producto4 = ProductoRopa("Pantalones", 30.0, 3, 3, "L", "Azul")
producto5 = ProductoElectronico("Ratón", 40.0, 4, 2, 5)
cliente1 = Cliente("Kelly","Kelly", "slater@gmail.com", 15174)
cliente2 = Cliente("Kelly","Irene", "ire305@hotmail.com", 9876)
cliente3 = Cliente("Kelly","Paloma", "palomita@gmail.com", 18975)
personal1 = Administrador("Kelly","Nata", "natamontadaconfresas@gmail.com", "alto")
pedido1= Pedido(cliente1, [(producto1, 1), (producto2, 2)])
pedido2 = Pedido(cliente2, [(producto3, 1), (producto4, 1)])
pedido3 = Pedido(cliente3, [(producto5, 1), (producto1, 1)])



print(pedido1)
print(pedido2)
print(pedido3)

