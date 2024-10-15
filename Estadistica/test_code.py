# test_large_code.py

class Calculator:
    """Clase para realizar operaciones matemáticas básicas."""
    
    def add(self, a, b):
        """Suma dos números."""
        return a + b

    def subtract(self, a, b):
        """Resta dos números."""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b

    def divide(self, a, b):
        """Divide dos números. Lanza un error si se divide por cero."""
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b


class Statistics:
    """Clase para realizar cálculos estadísticos."""
    
    @staticmethod
    def mean(data):
        """Calcula la media de una lista de números."""
        if len(data) == 0:
            return 0
        return sum(data) / len(data)

    @staticmethod
    def median(data):
        """Calcula la mediana de una lista de números."""
        n = len(data)
        sorted_data = sorted(data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    @staticmethod
    def mode(data):
        """Calcula la moda de una lista de números."""
        frequency = {}
        for number in data:
            frequency[number] = frequency.get(number, 0) + 1
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        return modes


def main():
    """Función principal para ejecutar las operaciones."""
    calc = Calculator()
    stats = Statistics()

    # Ejemplos de uso de la calculadora
    print("Calculadora:")
    print("Suma: 5 + 3 =", calc.add(5, 3))
    print("Resta: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplicación: 5 * 3 =", calc.multiply(5, 3))
    print("División: 5 / 2 =", calc.divide(5, 2))

    # Ejemplos de uso de estadísticas
    data = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
    print("\nEstadísticas:")
    print("Datos:", data)
    print("Media:", stats.mean(data))
    print("Mediana:", stats.median(data))
    print("Moda:", stats.mode(data))

    # Demostración de control de flujo
    print("\nControl de Flujo:")
    for i in range(10):
        if i % 2 == 0:
            print(f"{i} es par.")
        else:
            print(f"{i} es impar.")

    # Manejo de excepciones
    try:
        print("\nDivisión por cero:")
        print("5 / 0 =", calc.divide(5, 0))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
