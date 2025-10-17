"""
Este módulo contiene funciones para realizar operaciones matemáticas
y otras demostraciones de funciones en Python, incluyendo argumentos
predeterminados, *args, **kwargs, funciones lambda y recursivas.
"""

# Funciones Matemáticas Básicas

# Función sumar: Realiza la operación de suma
def sumar(a, b):
    """
    Suma dos números y retorna el resultado.

    Parámetros:
    a (int o float): Primer número.
    b (int o float): Segundo número.

    Retorna:
    int o float: Suma de a y b.
    """
    return a + b

# Función restar: Realiza la operación de resta
def restar(a, b=5):
    """
    Resta el segundo número del primero.
   
    Parámetros:
    a (int o float): Primer número.
    b (int o float, opcional): Segundo número, por defecto 5.

    Retorna:
    int o float: Resultado de a - b.
    """
    return a - b

# Función multiplicar: Realiza la operación de multiplicación
def multiplicar(*args):
    """
    Multiplica una cantidad variable de números.

    Parámetros:
    *args (int o float): Números a multiplicar.

    Retorna:
    int o float: Producto de todos los argumentos.
    """

    producto = 1
    for num in args:
        producto *= num
    return producto

# Función mostrar_info: 
def mostrar_info(**kwargs):
    """
    Muestra información variada utilizando argumentos de palabra clave.

    Parámetros:
        **kwargs (dict): Diccionario con datos como nombre, curso, edad.

    Imprime la información directamente.
    """
    # Itera sobre los pares clave-valor proporcionados.
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


# Función lambda para potencia
potencia = lambda base, exponente: base ** exponente

"""
Función lambda para calcular la potencia de un número.

Parámetros:
base (int o float): Base de la potencia.
exponente (int o float): Exponente de la potencia.

Retorna:
int o float: base elevado a exponente.
"""

# Función factorial:  

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Args:
        n (int): El número entero (no negativo).

    Returns:
        int: El factorial de 'n'.

    Raises:
        ValueError: Si 'n' es un número negativo.
    """
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("El factorial solo está definido para números no negativos.")
    else:
        return n * factorial(n - 1)