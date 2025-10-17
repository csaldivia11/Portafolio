"""Módulo con funciones para gestionar una colección de libros."""
from .libros import Libro
from .excepciones import LibroNoEncontradoError, IDExistenteError

def registrar_libro(libros_db, id_libro, titulo, autor, genero):
    """Añade un nuevo libro a la colección. Lanza IDExistenteError si el ID ya existe."""
    if id_libro in libros_db:
        raise IDExistenteError(f"Ya existe un libro con el ID '{id_libro}'.")
    
    nuevo_libro = Libro(id_libro, titulo, autor, genero)
    libros_db[id_libro] = nuevo_libro
    return f"Libro '{titulo}' registrado exitosamente."

def buscar_libro_por_id(libros_db, id_libro):
    """Busca un libro por su ID. Lanza LibroNoEncontradoError si no se encuentra."""
    libro = libros_db.get(id_libro)
    if not libro:
        raise LibroNoEncontradoError(f"No se encontró libro con ID: {id_libro}")
    return libro

def consultar_libros(libros_db, **kwargs):
    """Consulta libros según criterios variables (autor, genero, disponibilidad)."""
    if not kwargs:
        return list(libros_db.values())

    resultados = []
    for libro in libros_db.values():
        if all(getattr(libro, crit, None) == val for crit, val in kwargs.items()):
            resultados.append(libro)
    return resultados

def obtener_autores_unicos(libros_db):
    """Devuelve una lista ordenada de autores únicos de la base de datos de libros."""
    if not libros_db:
        return []
    autores_set = {libro.autor for libro in libros_db.values()}
    return sorted(list(autores_set))

def obtener_generos_unicos(libros_db):
    """Devuelve una lista ordenada de géneros únicos de la base de datos de libros."""
    if not libros_db:
        return []
    generos_set = {libro.genero for libro in libros_db.values()}
    return sorted(list(generos_set))