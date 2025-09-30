class Vector4D:
    def __init__(self, u: float, v: float, x: float, y: float):
        """
        Constructor: Inicialización de las coordenadas
        del vector en 4 Dimensiones
        """
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def __add__(self, vector):
        """
        Método especial que permite realizar una suma entre
        dos vectores utilizando el signo '+'
        """
        return self.u + vector.u, self.v + vector.v, self.x + vector.x, self.y + vector.y

    def __sub__(self, vector):
        """
        Método especial que permite restar un vector de otro utilizando el signo '-'
        """
        return self.u - vector.u, self.v - vector.v, self.x - vector.x, self.y - vector.y

    def __mul__(self, vector):
        """
        Método especial que permite multiplicar un vector por otro utilizando el signo '*'
        """
        return self.u * vector.u, self.v * vector.v, self.x * vector.x, self.y * vector.y

    def __truediv__(self, escalar: float):
        """
        Método especial que permite dividir un vector por un escalar utilizando el signo '/'
        """
        return self.u / escalar, self.v / escalar, self.x / escalar, self.y / escalar

vector_1 = Vector4D(2, 4, 6, 8)
vector_2 = Vector4D(1, 2, 3, 4)


print("Vector_1 + Vector_2 = ", vector_1 + vector_2)
print("Vector_1 - Vector_2 = ", vector_1 - vector_2)
print("Vector_1 * Vector_2 = ", vector_1 * vector_2)
print("Vector_2 / 2 = ", vector_2 / 2)