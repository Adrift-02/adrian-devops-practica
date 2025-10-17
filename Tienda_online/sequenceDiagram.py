sequenceDiagram
    actor Main as main.py
    participant ProdE as ProductoElectronico
    participant ProdR as ProductoRopa
    participant Prod as Producto
    participant Cliente as Cliente
    participant Ped as Pedido
    
    note over Main: Inicialización de Productos
    
    Main->>ProdE: __init__("Portatil", 1000.0, ...)
    activate ProdE
    ProdE->>Prod: super().__init__(...)
    deactivate ProdE
    
    Main->>ProdR: __init__("Sudadera", 20.0, ...)
    activate ProdR
    ProdR->>Prod: super().__init__(...)
    deactivate ProdR
    
    Main->>ProdE: __init__("Cargador", 25.0, ...)
    activate ProdE
    ProdE->>Prod: super().__init__(...)
    deactivate ProdE
    
    Main->>ProdR: __init__("Pantalones", 30.0, ...)
    activate ProdR
    ProdR->>Prod: super().__init__(...)
    deactivate ProdR
    
    Main->>ProdE: __init__("Ratón", 40.0, ...)
    activate ProdE
    ProdE->>Prod: super().__init__(...)
    deactivate ProdE
    
    note over Main: Creación de Clientes y Admin
    
    Main->>Cliente: __init__("Kelly", "slater@gmail.com", ...)
    
    Main->>Cliente: __init__("Irene", "ire305@hotmail.com", ...)
    
    Main->>Cliente: __init__("Paloma", "palomita@gmail.com", ...)
    
    
    note over Main: Creación de Pedidos
    
    Main->>Ped: __init__(cliente1, [(producto1, 1), (producto2, 2)])
    activate Ped
    Ped-->>Main: pedido1
    deactivate Ped
    
    Main->>Ped: __init__(cliente2, [(producto3, 1), (producto4, 1)])
    activate Ped
    Ped-->>Main: pedido2
    deactivate Ped
    
    Main->>Ped: __init__(cliente3, [(producto5, 1), (producto1, 1)])
    activate Ped
    Ped-->>Main: pedido3
    deactivate Ped
    
    note over Main: Impresión de Pedidos
    
    Main->>Ped: __str__()
    Ped-->>Main: (String de pedido1)
    
    Main->>Ped: __str__()
    Ped-->>Main: (String de pedido2)
    
    Main->>Ped: __str__()
    Ped-->>Main: (String de pedido3)