import math

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectangulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2
    
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8)
]

for figura in figuras:
    print(f"{figura.nombre}: Área = {figura.calcularArea():.2f}")


