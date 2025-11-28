from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr


from Services.Tienda_Service import Tienda_Service
from Models.Usuario import Usuario
from Models.producto import Producto, ProductoElectronico, ProductoRopa
from Models.pedido import Pedido

app = FastAPI(title="Tienda Online API (versión mínima)")

tienda_service = Tienda_Service()

# ---------------------- SCHEMAS ---------------------- #

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    tipo: str
    direccion_postal: Optional[str] = None


class UsuarioRead(BaseModel):
    id: UUID
    nombre: str
    email: EmailStr
    es_admin: bool 


# ----------- PRODUCTOS ----------- #
class ProductoBase(BaseModel):
    nombre: str
    precio: float
    cantidad: int

class ProductoElectronicoCreate(ProductoBase):
    garantia: int

class ProductoRopaCreate(ProductoBase):
    talla: str
    color: str

class ProductoRead(ProductoBase):
    id: UUID
    tipo: str
    extra: Optional[dict] = None


# ----------- PEDIDOS ----------- #
class PedidoItem(BaseModel):
    producto_id: UUID
    cantidad: int

class PedidoCreate(BaseModel):
    cliente_id: UUID
    items: List[PedidoItem]

class PedidoRead(BaseModel):
    id: str
    cliente_id: UUID
    fecha: datetime
    items: List[dict]
    numero_productos: int


# ---------------------- ENDPOINTS ---------------------- #

# ------ USUARIOS ------ #

@app.post("/usuarios", response_model=UsuarioRead)
def crear_usuario(datos: UsuarioCreate) -> UsuarioRead:
    try:
        usuario = tienda_service.registrar_usuario(
            nombre=datos.nombre,
            email=str(datos.email),
            tipo=datos.tipo,
            direccion_postal=datos.direccion_postal,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return UsuarioRead(
        id=usuario.id,
        nombre=usuario.nombre,
        email=usuario.email,
        es_admin=usuario.is_admin(),
    )


# ------ PRODUCTOS ------ #

@app.post("/productos/electronico", response_model=ProductoRead)
def crear_producto_electronico(datos: ProductoElectronicoCreate) -> ProductoRead:
    producto = ProductoElectronico(
        id=uuid4(),
        nombre=datos.nombre,
        precio=datos.precio,
        cantidad=datos.cantidad,
        garantia=datos.garantia,
    )
    tienda_service.productos[producto.id] = producto
    return ProductoRead(
        id=producto.id,
        nombre=producto.nombre,
        precio=producto.precio,
        cantidad=producto.cantidad,
        tipo="electronico",
        extra={"garantia": producto.garantia},
    )

@app.post("/productos/ropa", response_model=ProductoRead)
def crear_producto_ropa(datos: ProductoRopaCreate) -> ProductoRead:
    producto = ProductoRopa(
        id=uuid4(),
        nombre=datos.nombre,
        precio=datos.precio,
        cantidad=datos.cantidad,
        talla=datos.talla,
        color=datos.color,
    )
    tienda_service.productos[producto.id] = producto
    return ProductoRead(
        id=producto.id,
        nombre=producto.nombre,
        precio=producto.precio,
        cantidad=producto.cantidad,
        tipo="ropa",
        extra={"talla": producto.talla, "color": producto.color},
    )

@app.get("/productos", response_model=List[ProductoRead])
def listar_productos() -> List[ProductoRead]:
    productos = []
    for p in tienda_service.productos.values():
        tipo = "electronico" if isinstance(p, ProductoElectronico) else ("ropa" if isinstance(p, ProductoRopa) else "generico")
        extra = {}
        if tipo == "electronico":
            extra = {"garantia": getattr(p, "garantia", None)}
        elif tipo == "ropa":
            extra = {"talla": getattr(p, "talla", None), "color": getattr(p, "color", None)}
        productos.append(
            ProductoRead(
                id=p.id,
                nombre=p.nombre,
                precio=p.precio,
                cantidad=p.cantidad,
                tipo=tipo,
                extra=extra,
            )
        )
    return productos


# ------ PEDIDOS ------ #

@app.post("/pedidos", response_model=PedidoRead)
def crear_pedido(datos: PedidoCreate) -> PedidoRead:
    cliente = tienda_service.usuarios.get(datos.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    items = []
    for item in datos.items:
        producto = tienda_service.productos.get(item.producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto {item.producto_id} no encontrado")
        if producto.cantidad < item.cantidad:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para {producto.nombre}")
        producto.cantidad -= item.cantidad
        items.append((producto, item.cantidad))
    pedido = Pedido(cliente=cliente, items=items)
    tienda_service.pedidos[pedido.id] = pedido
    return PedidoRead(
        id=pedido.id,
        cliente_id=cliente.id,
        fecha=pedido.fecha,
        items=[{"producto_id": p.id, "nombre": p.nombre, "cantidad": c} for p, c in pedido.items],
        numero_productos=pedido.numero_productos,
    )

@app.get("/pedidos", response_model=List[PedidoRead])
def listar_pedidos() -> List[PedidoRead]:
    pedidos = []
    for p in tienda_service.pedidos.values():
        pedidos.append(
            PedidoRead(
                id=p.id,
                cliente_id=p.cliente.id,
                fecha=p.fecha,
                items=[{"producto_id": prod.id, "nombre": prod.nombre, "cantidad": cant} for prod, cant in p.items],
                numero_productos=p.numero_productos,
            )
        )
    return pedidos


@app.get("/usuarios", response_model=list[UsuarioRead])
def listar_usuarios() -> list[UsuarioRead]:
    # obtenemos todos los usuarios del servicio
    usuarios = tienda_service.usuarios.values()

    # convertimos cada uno al schema UsuarioRead
    return [
        UsuarioRead(
            id=u.id,
            nombre=u.nombre,
            email=u.email,
            es_admin=u.is_admin(),
        )
        for u in usuarios
    ]


@app.get("/usuarios/{usuario_id}", response_model=UsuarioRead)
def obtener_usuario(usuario_id: UUID) -> UsuarioRead:
    try:
        usuario = tienda_service.obtener_usuario(usuario_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return UsuarioRead(
        id=usuario.id,
        nombre=usuario.nombre,
        email=usuario.email,
        es_admin=usuario.is_admin(),
    )
