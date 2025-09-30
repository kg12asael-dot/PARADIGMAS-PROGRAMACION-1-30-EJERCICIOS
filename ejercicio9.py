class Vehiculo:
    def __init__(self, marca: str, velocidad_i: float = 0):
        """
        Constructor para inicializar los atributos:
        marca ::: str : la marca del coche
        velocidad_i ::: float : la velocidad inicial del coche
        >>> velocidad_i tiene un valor predeterminado = 0
        """
        self.marca = marca
        self.velocidad = velocidad_i

    def acelerar(self, v: float):
        """
        Este método permite aumentar la velocidad del coche.
        """
        self.velocidad += v

    def desacelerar(self, v: float):
        """
        Este método permite disminuir la velocidad del coche.
        """
        self.velocidad -= v

    def mostrar_velocidad(self):
        """
        Este método permite mostrar la velocidad actual del coche.
        """
        print(f"Tu velocidad actual es: {self.velocidad} km/h")


class Coche(Vehiculo):
    def __init__(self, marca: str, velocidad_i: float = 0, bocina: str = "tuuut !"):
        """
        Constructor para inicializar los atributos de la clase hija
        """
        
        super().__init__(marca, velocidad_i)
        
        self.bocina = bocina

    def tocar_claxon(self):
        """
        Este método permite tocar la bocina, devolviendo una cadena de caracteres.
        """
        print(self.bocina)


coche_1 = Coche("Peugeot 208", 10.5)


print("La velocidad inicial del coche es:", coche_1.velocidad, "km/h")


coche_1.acelerar(50)
coche_1.desacelerar(15)
coche_1.mostrar_velocidad()
coche_1.tocar_claxon()