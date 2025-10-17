"""Módulo que contiene la clase Libro."""

class Libro:
    """
    Representa un libro en la biblioteca.
    """
    def __init__(self, id_libro, titulo, autor, genero, disponible=True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible

    def __str__(self):
        """Representación legible del objeto Libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id_libro} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"