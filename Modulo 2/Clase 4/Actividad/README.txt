Actividad Programación Orientada a Objeto 

El código define dos clases para modelar un sistema simple de gestión de usuarios:

Clase Usuario_
Atributos
nombre: El nombre del usuario (público).
correo: El correo electrónico del usuario (público).
__contraseña: La contraseña del usuario (privada). El doble guion bajo indica que es un atributo de uso interno.

Métodos:
- saludar(): Devuelve un saludo personalizado.
- mostrar_info(): Devuelve un string con el nombre y correo del usuario.
- contraseña (@property y @setter): Métodos especiales para acceder y modificar el atributo privado `__contraseña`.

Clase Administrador: Hereda de la clase Usuario, lo que significa que un Administrador es un Usuario y, por lo tanto, tiene todas sus características.
Atributos
- Hereda (nombre, correo y __contraseña)-
- permisos: Un es una lista para almacenar los permisos del administrador.

Métodos**:
- mostrar_info(): Redefine el método de la clase padre para incluir también la lista de permisos.
- agregar_permiso(): Un método nuevo y específico para añadir permisos a la lista.

La parte final del script demuestra cómo se utilizan estas clases:
1.  Se crean dos objetos: usuario1 (de la clase Usuario) y admin1 (de la clase Administrador).
2.  Se llama a los métodos saludar() y mostrar_info() en ambos, demostrando la herencia y el polimorfismo.
3.  Se utiliza el setter para cambiar la contraseña de usuario1 y el getter para imprimirla.
4.  Se utiliza el método agregar_permiso(), que solo existe en la clase Administrador, y se vuelve a mostrar la información para ver el cambio.