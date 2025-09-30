class Computadora:
    def __init__(self, marca: str, modelo: str, precio: float):
        """
        Constructor para inicializar las variables
        de instancia
        """
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    @staticmethod
    def listar_marcas():
        """
        Este método estático permite devolver las
        marcas disponibles
        """
        return "Dell, HP, Lenovo, Apple"


class ComputadorEscritorio(Computadora):
    def __init__(self, marca: str, modelo: str, precio: float, tamano_unidad_central: str):
        """
        Constructor que permite inicializar los atributos
        de la clase OrdenadorDeMesa
        """
        super().__init__(marca, modelo, precio)
        self.tamano_unidad_central = tamano_unidad_central

    def mostrar_informacion(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de esta clase
        """
        return (f"La computadora de escritorio de la marca {self.marca} ({self.modelo}) - "
                f"con una unidad central de tamaño {self.tamano_unidad_central} - "
                f"cuesta {self.precio} euros.")


class ComputadoraPortatil(Computadora):
    def __init__(self, marca: str, modelo: str, precio: float, tamano_pulgadas: float):
        """
        Constructor
        """
        super().__init__(marca, modelo, precio)
        self.tamano_pulgadas = tamano_pulgadas

    def mostrar_informacion(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de esta clase
        """
        return (f"La computadora portátil de la marca {self.marca} ({self.modelo}) "
                f"con una pantalla de {self.tamano_pulgadas} pulgadas cuesta {self.precio} euros.")



print("Las marcas de computadoras disponibles son:", Computadora.listar_marcas())


ordenador_escritorio = ComputadorEscritorio("Dell", "78L", 800, "5L")
computador_portatil = ComputadoraPortatil("HP", "X1A", 950, 15.6)

print(ordenador_escritorio.mostrar_informacion())
print(computador_portatil.mostrar_informacion())