# test_large_code.py

def calculate_sum(a, b):
    """Calcula la suma de dos números."""
    return a + b

def calculate_product(a, b):
    """Calcula el producto de dos números."""
    return a * b

def is_even(number):
    """Determina si un número es par."""
    return number % 2 == 0

def fibonacci(n):
    """Genera la serie de Fibonacci hasta n."""
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def factorial(n):
    """Calcula el factorial de n de manera recursiva."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Función principal del programa."""
    print("Sum:", calculate_sum(5, 3))
    print("Product:", calculate_product(5, 3))
    print("Is 4 even?", is_even(4))
    print("Fibonacci sequence up to 10:", fibonacci(10))
    print("Factorial of 5:", factorial(5))

if __name__ == "__main__":
    main()

# Comentarios de ejemplo
# Este es un ejemplo de archivo de prueba con diversas funciones y comentarios.
# Las siguientes funciones son parte de una simple calculadora.
# Adicionalmente, se incluye un ejemplo de función recursiva (factorial).
