Actividad Estructuras de Datos e Iteraciones en Python 

Este documento detalla la funcionalidad del script estructuras_iteraciones.py.
El propósito del script es usar listas, diccionarios, tuplas, sets y ciclos (for y while) en Python para crear scripts que resuelvan tareas básicas de manejo de datos.  

Bloque 1 – Listas y Listas Anidadas
- Creación de Lista Heterogénea: Se inicializa una variable llamada lista que contiene cinco elementos de distintos tipos de datos.
- Se utiliza el método .append("Ingenieria datos") para agregar un nuevo elemento (una cadena de texto) al final de la lista.
- Se utiliza .remove(30) para buscar y eliminar la primera aparición del valor 30 de la lista.
- Acceso a Elementos: Se demuestra el acceso a elementos específicos mediante sus índices. Se imprime el primer elemento con lista[0] y el último con lista[-1].
- Lista Anidada (Matriz): Se crea una variable matriz que es una lista de listas, simulando una matriz de 3x3. 
                          Para acceder a la segunda fila, se utiliza el índice 1 (matriz[1]).

Bloque 2 – Diccionarios y Diccionarios Anidados
Creación de Diccionario: Se crea un diccionario llamado estudiante utilizando llaves {}. Almacena información personal mediante pares clave.
Adición de un Nuevo Par: Se agrega una nueva clave "notas" al diccionario y se le asigna una lista de tres calificaciones flotantes.
Acceso a Datos: Se accede a la carrera del estudiante usando su clave estudiante["carrera"].

Bloque 3 – Tuplas y Empaquetado/Desempaquetado
Creación de Tupla: Se crea una tupla llamada libro con los datos de "El imperio final" de Brandon Sanderson.
Desempaquetado de Tupla: Se realiza una de las operaciones más elegantes con tuplas.
Uso de Datos Desempaquetados: Las variables recién creadas se utilizan dentro de una cadena formateada (f-string) para imprimir una frase descriptiva sobre el libro.

Bloque 4 – Sets y Operaciones de Conjunto
Creación de Sets: Se crean dos conjuntos, set_a y set_b, a partir de listas que contienen elementos duplicados. La función set() elimina automáticamente estos duplicados.
Operaciones de Conjunto: Se realizan dos operaciones matemáticas comunes con sets:
Unión (|): Crea un nuevo conjunto que contiene todos los elementos únicos de set_a y set_b combinados.
Intersección (&): Crea un nuevo conjunto que contiene únicamente los elementos que están presentes en ambos conjuntos (set_a y set_b).

Bloque 5 – Iteraciones
Bucle for con una Lista: Se utiliza un bucle for para iterar sobre cada nombre en la lista nombres. En cada iteración, se imprime un saludo personalizado.
Bucle for con range(): Se utiliza la función range(1, 11) para generar una secuencia de números del 1 al 10.
Bucle for con un Diccionario: Se itera sobre el diccionario estudiante usando el método .items(), que devuelve cada par clave-valor. En cada paso del bucle, estos se desempaquetan en las variables clave y valor.
Bucle while: Se implementa un bucle while para calcular la suma de los números del 1 al 5. El bucle se ejecuta repetidamente mientras la condición contador <= 5 sea verdadera.