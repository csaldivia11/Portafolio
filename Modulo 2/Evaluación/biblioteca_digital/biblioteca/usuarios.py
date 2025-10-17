"""Módulo que contiene las clases Usuario, Estudiante e Instructor."""

class Usuario:
    """
    Representa un usuario del sistema con atributos de acceso directo.
    """
    def __init__(self, id_usuario, nombre, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        """Representación legible del objeto Usuario."""
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Rol: {self.rol}"

class Estudiante(Usuario):
    """Clase para usuarios con rol 'Estudiante', hereda de Usuario."""
    def __init__(self, id_usuario, nombre):
        super().__init__(id_usuario, nombre, "Estudiante")

class Instructor(Usuario):
    """Clase para usuarios con rol 'Instructor', hereda de Usuario."""
    def __init__(self, id_usuario, nombre):
        super().__init__(id_usuario, nombre, "Instructor")