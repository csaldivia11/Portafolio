"""Módulo para gestionar los préstamos."""
from .prestamos import Prestamo
from .excepciones import LibroNoDisponibleError, PrestamoDuplicadoError
from .gestion_libros import buscar_libro_por_id
from .gestion_usuarios import buscar_usuario_por_id

def realizar_prestamo(libros_db, usuarios_db, prestamos_db, id_libro, id_usuario):
    """Gestiona el préstamo de un libro, realizando todas las validaciones."""
    libro = buscar_libro_por_id(libros_db, id_libro)
    usuario = buscar_usuario_por_id(usuarios_db, id_usuario)

    if not libro.disponible:
        raise LibroNoDisponibleError(f"El libro '{libro.titulo}' ya se encuentra prestado.")

    for prestamo in prestamos_db:
        if prestamo.id_libro == id_libro and prestamo.id_usuario == id_usuario:
            raise PrestamoDuplicadoError()

    libro.disponible = False
    nuevo_prestamo = Prestamo(id_libro, id_usuario)
    prestamos_db.append(nuevo_prestamo)
    
    return f"Préstamo realizado: '{libro.titulo}' a {usuario.nombre}."

def listar_libros_prestados(libros_db):
    """Devuelve una lista de los libros que figuran como no disponibles."""
    return [libro for libro in libros_db.values() if not libro.disponible]