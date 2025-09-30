class TrabajadorEmpresa:
    def __init__(self, nombre_trabajador: str, salario: float, edad: int):
        """
        Constructor: Inicialización de los atributos de la
        clase TrabajadorEmpresa
        """
        self.nombre_trabajador = nombre_trabajador
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self):
        """
        Este método permite mostrar la función del objeto
        proveniente de esta clase
        """
        print("Soy un trabajador en una empresa")

    def mostrar_info(self):
        """
        Este método permite mostrar la información relacionada
        con el trabajador
        """
        print(f"Nombre: {self.nombre_trabajador}")
        print(f"Salario: {self.salario}")
        print(f"Edad: {self.edad}")


class Director(TrabajadorEmpresa):
    def __init__(self, nombre_director: str, salario: float, edad: int, prima: float):
        """
        Este método permite inicializar los atributos de la
        clase Director
        """
        super().__init__(nombre_director, salario, edad)
        self.prima = prima

    def mostrar_funcion(self):
        """
        Este método muestra la función del objeto
        proveniente de la clase Director
        """
        print("Soy un director de empresa")

    def mostrar_info(self):
        """
        Este método permite mostrar la información
        concerniente al objeto de esta clase
        """
        super().mostrar_info()
        print(f"La prima anual percibida es de {self.prima} euros.")


class Ingeniero(TrabajadorEmpresa):
    def __init__(self, nombre_ingeniero: str, salario: float, edad: int, especialidad: str):
        """
        Constructor: Inicializar los atributos de la clase
        """
        super().__init__(nombre_ingeniero, salario, edad)
        self.especialidad = especialidad

    def mostrar_funcion(self):
        """
        Este método permite mostrar la función del objeto
        proveniente de esta clase
        """
        print("Soy ingeniero")

    def mostrar_info(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de la clase
        """
        super().mostrar_info()
        print(f"Soy un Ingeniero especializado en {self.especialidad}")

director = Director("Julien Lecoq", 75000, 43, 5000)
ingeniero = Ingeniero("Baptiste Leblanc", 40000, 32, "Inteligencia Artificial")

trabajadores = [director, ingeniero]

for trabajador in trabajadores:
    trabajador.mostrar_funcion()
    trabajador.mostrar_info()
    print() 