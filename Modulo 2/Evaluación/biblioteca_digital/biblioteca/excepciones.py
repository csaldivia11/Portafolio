"""Módulo para definir excepciones personalizadas de la biblioteca."""

class IDExistenteError(Exception):
    """Excepción para cuando se intenta registrar un recurso con un ID que ya existe."""
    def __init__(self, mensaje="El ID proporcionado ya existe en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class LibroNoEncontradoError(Exception):
    """Excepción para cuando un libro no se encuentra en la base de datos."""
    def __init__(self, mensaje="El libro solicitado no se encuentra en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class UsuarioNoRegistradoError(Exception):
    """Excepción para cuando un usuario no está registrado."""
    def __init__(self, mensaje="El usuario no está registrado en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class PrestamoDuplicadoError(Exception):
    """Excepción para cuando se intenta prestar un libro que el usuario ya tiene."""
    def __init__(self, mensaje="Este usuario ya tiene un préstamo activo de este libro."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class LibroNoDisponibleError(Exception):
    """Excepción para cuando un libro existe pero no está disponible."""
    def __init__(self, mensaje="El libro solicitado no está disponible actualmente."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)