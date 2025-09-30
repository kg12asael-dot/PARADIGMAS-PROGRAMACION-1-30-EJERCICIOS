class Calculadora:
    def __init__(self, variable: float):
        """
        Constructor
        """
        self.variable = variable

    @staticmethod
    def suma(x: float, y: float):
        """
        Método estático que permite calcular la suma de
        dos valores
        """
        return x + y

    @staticmethod
    def multiplicacion(x: float, y: float):
        """
        Método estático que permite calcular el producto
        de dos valores
        """
        return x * y

    @staticmethod
    def division(x: float, y: float):
        """
        Método estático que permite calcular la división
        de x por y
        """
        if y == 0:
            return "Operación imposible"
        else:
            return x / y

c1 = Calculadora(10)

print("Suma de dos números:", Calculadora.suma(2, 4))
print("Multiplicación de dos números:", Calculadora.multiplicacion(4, 8))
print("División de dos números:", Calculadora.division(4, 2))
print("Suma de dos números usando una instancia de clase:", c1.suma(3, 8))