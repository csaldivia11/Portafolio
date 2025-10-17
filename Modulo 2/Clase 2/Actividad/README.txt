Actividad Funciones y Módulos en Python

Esta actividad trabaja el uso de funciones y módulos en Python.

Archivos del Proyecto

operaciones.py: Contiene la definición de todas las funciones matemáticas y demostrativas, cada una con su docstring y comentarios internos.
main.py: Es el script principal que importa las funciones de `operaciones.py`, solicita entrada al usuario, llama a las funciones y muestra los resultados.

Desarrollo del Código

operaciones.py
- sumar(a, b): Suma dos números.
- restar(a, b=5): Resta, demostrando el argumento predeterminado b=5.
- multiplicar(*args): Multiplica una cantidad variable de números, utilizando *args para aceptar cualquier número de argumentos posicionales.
- mostrar_info(**kwargs): Muestra información utilizando **kwargs para aceptar cualquier número de argumentos de palabra clave (nombre, curso, edad, etc.).
- potencia = lambda base, exponente: base ** exponente: Una función lambda simple para calcular la potencia.
- factorial(n): Una función recursiva para calcular el factorial de un número. Incluye manejo para números negativos.

main.py
- Importa el módulo operaciones.py.
- Solicita al usuario dos números para las operaciones.
- Llama a cada una de las funciones definidas en operaciones.py con ejemplos de uso.
- Imprime los resultados de cada operación de manera clara.
- Incluye manejo básico de errores para la entrada del usuario.