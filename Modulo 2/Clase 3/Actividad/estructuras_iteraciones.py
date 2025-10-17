# Bloque 1: Listas y Listas Anidadas ---
print("\nBloque 1: Listas y Listas Anidadas")

# Crear una lista con al menos 5 elementos de diferentes tipos
lista = [30, "Carlos", True, 3.1416, (5,10)]
print(f"\nLista original: {lista}")

# Agregar un elemento
lista.append("Ingenieria datos")
print(f"Lista tras agregar un elemento: {lista}")

# Eliminar un elemento
lista.remove(30)
print(f"Lista tras eliminar el elemento '30': {lista}")

# Acceder al primer y último elemento
print(f"Primer elemento: {lista[0]}")
print(f"Último elemento: {lista[-1]}")

# Crear una lista anidada (matriz de 3x3) e imprimir su segunda fila
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz 3x3: {matriz}")
print(f"Segunda fila de la matriz: {matriz[1]}")

#Bloque 2: Diccionarios y Diccionarios Anidados
print("\nBloque 2: Diccionarios y Diccionarios Anidados")

# Crear un diccionario con datos de un estudiante
estudiante = {
    "nombre": "Carlos",
    "edad": 30,
    "carrera": "Ingeniería de Datos"
}
print(f"\nDiccionario del estudiante: {estudiante}")

# Agregar una clave 'notas' con una lista de 3 notas
estudiante["notas"] = [6.2, 6.8, 7.0]
print(f"Diccionario con notas agregadas: {estudiante}")

# Imprimir la segunda nota y la carrera del estudiante
segunda_nota = estudiante["notas"][1]
carrera_estudiante = estudiante["carrera"]
print(f"La segunda nota del estudiante es: {segunda_nota}")
print(f"La carrera del estudiante es: {carrera_estudiante}")

# Bloque 3: Tuplas y Empaquetado/Desempaquetado
print("\nBloque 3: Tuplas y Empaquetado/Desempaquetado")

# Crear una tupla con datos de un libro
libro = ("El imperio final", "Brandon Sanderson", 2008)
print(f"\nTupla del libro: {libro}")

# Desempaquetar la tupla en tres variables
titulo, autor, anio = libro

# Imprimir una frase usando los datos desempaquetados
print(f'El libro "{titulo}", escrito por {autor}, fue publicado en el año {anio}.')

# Bloque 4: Sets y Operaciones de Conjunto
print("\nBloque 4: Sets y Operaciones de Conjunto")

# Se crean a partir de listas con duplicados para demostrar cómo los sets los eliminan
lista_a = [1, 2, 3, 3, 4, 5]
lista_b = [4, 5, 6, 7, 7, 8]

# Crear dos conjuntos
set_a = set(lista_a)
set_b = set(lista_b)
print(f"\nConjunto A (sin duplicados): {set_a}")
print(f"Conjunto B (sin duplicados): {set_b}")

# Realizar e imprimir la intersección y la unión
union = set_a | set_b
interseccion = set_a & set_b
print(f"Unión de A y B: {union}")
print(f"Intersección de A y B: {interseccion}")

# Bloque 5: Iteraciones
print("\nBloque 5: Iteraciones")

# Iterar una lista de nombres usando for
print("\nSaludos con un bucle for:")
nombres = ["Ana", "Juan", "Pedro"]
for nombre in nombres:
    print(f"¡Hola, {nombre}!")

# Usar range para imprimir los números del 1 al 10
print("\nNúmeros del 1 al 10 con 'range':")
for i in range(1, 11):
    print(i)

# Iterar un diccionario imprimiendo las claves y los valores
print("\nIterando el diccionario estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave.capitalize()}: {valor}")

# Usar un ciclo while para sumar los números del 1 al 5
print("\nSumando números del 1 al 5 con while:")
suma = 0
contador = 1
while contador <= 5:
    suma += contador
    contador += 1
print(f"La suma total es: {suma}")