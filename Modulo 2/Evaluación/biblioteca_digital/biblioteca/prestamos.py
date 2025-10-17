"""Módulo que contiene la clase Prestamo."""
from datetime import date

class Prestamo:
    """
    Representa el acto de prestar un libro a un usuario.
    """
    def __init__(self, id_libro, id_usuario, fecha_prestamo=None):
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo is not None else date.today()

    def __str__(self):
        """Representación legible del objeto Prestamo."""
        return f"Libro ID: {self.id_libro} | Usuario ID: {self.id_usuario} | Fecha: {self.fecha_prestamo}"