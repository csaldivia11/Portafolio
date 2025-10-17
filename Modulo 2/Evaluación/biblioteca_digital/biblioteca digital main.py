"""
Script principal del sistema de gestión de biblioteca.
"""
# Importamos los módulos necesarios de nuestro paquete biblioteca
from biblioteca import (
    gestion_libros,
    gestion_usuarios,
    gestion_prestamos,
    libros,
    usuarios,
    prestamos,
    excepciones
)

# Carga de datos iniciales para probar script
def cargar_datos_iniciales():
    """Crea y retorna las colecciones iniciales de datos para la demo."""
    db_libros = {
        "101": libros.Libro("101", "Python para Todos", "Charles R. Severance", "Programación"),
        "201": libros.Libro("201", "El resplandor", "Stephen King", "Novela"),
        "202": libros.Libro("202", "El Señor de los Anillos", "J.R.R. Tolkien", "Novela", disponible=False)
    }

    db_usuarios = {
        "E001": usuarios.Estudiante("E001", "Carlos"),
        "I001": usuarios.Instructor("I001", "Mario")
    }
    
    db_prestamos = [prestamos.Prestamo("202", "E001")]
    
    return db_libros, db_usuarios, db_prestamos

# Funciones Auxiliares
def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n" + "-"*34)
    print("--- Menú de Biblioteca Digital ---")
    print("1. Registrar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Consultar usuarios")
    print("4. Consultar libros por autor")
    print("5. Consultar libros por género")
    print("6. Consultar libros disponibles")
    print("7. Realizar un préstamo")
    print("8. Listar libros prestados")
    print("0. Salir")
    print("-"*34)

def pedir_datos_libro():
    """Solicita y retorna los datos para un nuevo libro."""
    return input("ID: "), input("Título: "), input("Autor: "), input("Género: ")

def pedir_datos_usuario():
    """Solicita y retorna los datos para un nuevo usuario."""
    return input("ID: "), input("Nombre: "), input("Rol (estudiante/instructor): ")

def imprimir_resultados(resultados, mensaje_vacio):
    """Imprime una lista de resultados o un mensaje si está vacía."""
    if resultados:
        for item in resultados:
            print(item)
    else:
        print(mensaje_vacio)

# Función principal
def main():
    """Función principal que ejecuta el bucle del programa."""
    libros_db, usuarios_db, prestamos_db = cargar_datos_iniciales()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_l, titulo, autor, genero = pedir_datos_libro()
                mensaje = gestion_libros.registrar_libro(libros_db, id_l, titulo, autor, genero)
                print(mensaje)

            elif opcion == "2":
                id_u, nombre, rol = pedir_datos_usuario()
                mensaje = gestion_usuarios.registrar_usuario(usuarios_db, id_u, nombre, rol)
                print(mensaje)
            
            elif opcion == "3":
                print("\n--- Usuarios Registrados ---")
                resultados = gestion_usuarios.listar_usuarios(usuarios_db)
                imprimir_resultados(resultados, "No hay usuarios registrados.")

            elif opcion == "4":
                autores_disponibles = gestion_libros.obtener_autores_unicos(libros_db)
                if not autores_disponibles:
                    print("\nNo hay autores registrados en la biblioteca.")
                    continue
                
                print("\n--- Autores Disponibles ---")
                for autor_item in autores_disponibles:
                    print(f"- {autor_item}")
                
                autor = input("\nIngrese el nombre del autor a buscar: ")
                resultados = gestion_libros.consultar_libros(libros_db, autor=autor)
                print("\nResultados de la búsqueda:")
                imprimir_resultados(resultados, f"No se encontraron libros del autor '{autor}'.")

            elif opcion == "5": 
                generos_disponibles = gestion_libros.obtener_generos_unicos(libros_db)
                if not generos_disponibles:
                    print("\nNo hay géneros registrados en la biblioteca.")
                    continue

                print("\n--- Géneros Disponibles ---")
                for genero_item in generos_disponibles:
                    print(f"- {genero_item}")

                genero = input("\nIngrese el género a buscar: ")
                resultados = gestion_libros.consultar_libros(libros_db, genero=genero)
                print("\nResultados de la búsqueda:")
                imprimir_resultados(resultados, f"No se encontraron libros del género '{genero}'.")

            elif opcion == "6":
                print("\n--- Libros Disponibles ---")
                resultados = gestion_libros.consultar_libros(libros_db, disponible=True)
                imprimir_resultados(resultados, "No hay libros disponibles en este momento.")

            elif opcion == "7":
                id_l = input("ID del libro a prestar: ")
                id_u = input("ID del usuario que presta: ")
                mensaje = gestion_prestamos.realizar_prestamo(libros_db, usuarios_db, prestamos_db, id_l, id_u)
                print(mensaje)

            elif opcion == "8":
                print("\n--- Libros Prestados Actualmente ---")
                resultados = gestion_prestamos.listar_libros_prestados(libros_db)
                imprimir_resultados(resultados, "No hay libros prestados actualmente.")
            
            elif opcion == "0":
                print("Gracias por usar la Biblioteca Digital. ¡Hasta pronto!")
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        except (excepciones.LibroNoEncontradoError, 
                excepciones.UsuarioNoRegistradoError, 
                excepciones.LibroNoDisponibleError,
                excepciones.PrestamoDuplicadoError,
                excepciones.IDExistenteError,
                ValueError) as e:
            print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()