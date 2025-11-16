class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"

class Cliente(Usuario):
    def __init__(self, id, nombre, email, direccion_postal):
        super().__init__(id, nombre, email)
        self.direccion_postal = direccion_postal

    def __str__(self):
        return f"{super().__str__()}, Dirección Postal: {self.direccion_postal}"

    def is_admin(self):
        return False

class Administrador(Usuario):
    def __init__(self, id, nombre, email, nivel_acceso):
        super().__init__(id, nombre, email)
        self.nivel_acceso = nivel_acceso

    def __str__(self):
        return f"{super().__str__()}, Nivel de Acceso: {self.nivel_acceso}"

    def is_admin(self):
        return True
