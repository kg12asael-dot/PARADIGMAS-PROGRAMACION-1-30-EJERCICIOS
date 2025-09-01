class Paleta:
    def __init__(self, sabor: str, precio: float):
        self.sabor = sabor
        self.precio = precio

    def mostrarInformacion(self):
        print(f"Sabor: {self.sabor}, Precio: ${self.precio:.2f}")

class PaletaAgua(Paleta):
    def __init__(self, sabor: str, precio: float, baseAgua: bool):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua
        self.precio += 2

    def mostrarBaseAgua(self):
        print("Base de agua:", "Sí" if self.baseAgua else "No")

class PaletaCrema(Paleta):
    def __init__(self, sabor: str, precio: float, cremosa: bool):
        super().__init__(sabor, precio)
        self.cremosa = cremosa
        self.precio += 6

    def mostrarTexturaCremosa(self):
        print("Textura cremosa:", "Sí" if self.cremosa else "No")


    def aplicarDescuento(self, porcentaje: float):
        self.precio *= (1 - porcentaje / 100)

    def cambiarSabor(self, nuevo_sabor: str):
        self.sabor = nuevo_sabor


agua = PaletaAgua("Limón", 10.0, True)
agua.mostrarInformacion()
agua.mostrarBaseAgua()

crema = PaletaCrema("Chocolate", 12.0, True)
crema.mostrarInformacion()
crema.mostrarTexturaCremosa()

crema.aplicarDescuento(15)
crema.cambiarSabor("Avellana")
crema.mostrarInformacion()


