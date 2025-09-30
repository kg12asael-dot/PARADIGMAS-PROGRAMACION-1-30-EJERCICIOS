class Animal:
    def __init__(self, nombre_Animal: str):
        """
        Constructor de la clase Animal
        """
        self.nombre_animal = nombre_Animal

    def hablar(self):
        """
        Este método está vacío.
        Solo sirve para ilustrar el polimorfismo.
        """
        pass


class Gato(Animal):
    def __init__(self, nombre_gato: str):
        """
        Constructor
        """
        super().__init__(nombre_gato)

    def hablar(self):
        """
        Este método devuelve una cadena de caracteres
        que hace referencia al perro
        """
        return self.nombre_animal + " dice ¡Miau miau!"


class Perro(Animal):
    def __init__(self, nombre_perro: str):
        """
        Constructor
        """
        super().__init__(nombre_perro)

    def hablar(self):
        """
        Este método devuelve una cadena de caracteres
        que hace referencia al perro
        """
        return self.nombre_animal + " dice ¡Guau guau!"

rocky = Perro("Rocky")
felix = Gato("Felix")

print(rocky.hablar())
print(felix.hablar())