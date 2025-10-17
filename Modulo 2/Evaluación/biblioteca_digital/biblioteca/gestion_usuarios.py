"""Módulo con funciones para gestionar una colección de usuarios."""
from .usuarios import Estudiante, Instructor
from .excepciones import UsuarioNoRegistradoError, IDExistenteError

def registrar_usuario(usuarios_db, id_usuario, nombre, rol="estudiante"):
    """Añade un nuevo usuario. Lanza IDExistenteError o ValueError."""
    if id_usuario in usuarios_db:
        raise IDExistenteError(f"Ya existe un usuario con el ID '{id_usuario}'.")

    rol_lower = rol.lower()
    if rol_lower == "estudiante":
        nuevo_usuario = Estudiante(id_usuario, nombre)
    elif rol_lower == "instructor":
        nuevo_usuario = Instructor(id_usuario, nombre)
    else:
        raise ValueError("Rol no válido. Debe ser 'estudiante' o 'instructor'.")
    
    usuarios_db[id_usuario] = nuevo_usuario
    return f"Usuario '{nombre}' registrado como {nuevo_usuario.rol}."

def buscar_usuario_por_id(usuarios_db, id_usuario):
    """Busca un usuario por su ID. Lanza UsuarioNoRegistradoError si no se encuentra."""
    usuario = usuarios_db.get(id_usuario)
    if not usuario:
        raise UsuarioNoRegistradoError(f"No se encontró usuario con ID: {id_usuario}")
    return usuario

def listar_usuarios(usuarios_db):
    """Devuelve una lista de todos los usuarios registrados."""
    if not usuarios_db:
        return []
    return list(usuarios_db.values())