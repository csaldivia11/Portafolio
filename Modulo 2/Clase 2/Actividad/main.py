# Exploración de Funciones y Módulos:

# ¿Qué es una función en Python?
# Una función en Python es un bloque de código reutilizable diseñado para realizar una tarea específica.
# Ayuda a organizar el código, hacerlo más legible y evitar la repetición.
# Se define con la palabra clave def.

# ¿Qué es un módulo y para qué sirve?
# Un módulo en Python es un archivo (.py) que contiene definiciones de Python (funciones, clases, variables).
# Sirve para organizar el código en unidades lógicas y reutilizables.
# Permite agrupar código relacionado y facilita su importación y uso en otros scripts o módulos.

# ¿Qué ventajas tiene modularizar el código?
# Las ventajas de modularizar el código incluyen:
# 1- Reutilización de código sin repetirlo
# 2- Mantenimiento más sencillo y localizado
# 3- Facilita la colaboración en equipo
# 4- Mejora la legibilidad y organización
# 5- Permite mayor escalabilidad del proyecto
# 6- Facilita las pruebas unitarias

# ¿Qué es un docstring y cómo se usa?
# Un docstring (del inglés "documentation string") es una cadena literal que aparece como la primera declaración en un módulo, clase, función o método.
# Se usa para documentar el propósito y el uso del bloque de código al que pertenece.
# Se encierra entre comillas triples (simples o dobles).

import operaciones

# Pedir al usuario ingresar dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamar a las funciones y mostrar resultados

# Suma
resultado_suma = operaciones.sumar(num1, num2)
print(f"\nResultado de la suma ({num1} + {num2}): {resultado_suma}")

# Resta (demostrando argumento predeterminado)
# Llamada completa con dos argumentos
resultado_resta_completa = operaciones.restar(num1, num2)
print(f"\nResultado de la resta ({num1} - {num2}): {resultado_resta_completa}")
# Llamada utilizando el argumento predeterminado para 'b' (b=5)
resultado_resta_default = operaciones.restar(num1)
print(f"\nResultado de la resta (Valor predeterminado b=5) ({num1} - 5): {resultado_resta_default}")

# Multiplicación (*args)
# Demostrando flexibilidad con diferentes cantidades de argumentos
resultado_mult_2 = operaciones.multiplicar(num1, num2)
print(f"\nResultado de la multiplicación ({num1} * {num2}): {resultado_mult_2}")

# Potencia (lambda)
resultado_potencia = operaciones.potencia(num1, num2)
print(f"\nResultado de la potencia ({num1} elevado a la {num2}): {resultado_potencia}")

# Factorial (recursiva)
# Aseguramos que el número sea entero para el factorial
num_factorial = int(num1) # Usamos el primer número para el factorial
if num_factorial >= 0:
    resultado_factorial = operaciones.factorial(num_factorial)
    print(f"\nResultado del factorial de {num_factorial}: {resultado_factorial}")
else:
    print(f"\nNo se puede calcular el factorial de {num_factorial} (número negativo).")

# Mostrar información (**kwargs)
operaciones.mostrar_info(
    nombre="Carlos Saldivia",
    curso="Ingeniería de Datos",
    edad=30,
    ciudad="Santiago"
)