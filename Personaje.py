class Personaje:
    def __init__(self, nombre: str, nivel: int):
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        print(f"{self.nombre} ataca con fuerza nivel {self.nivel}.")

class Jugador(Personaje):
    def __init__(self, nombre: str, nivel: int, clase: str):
        super().__init__(nombre, nivel)
        self.clase = clase

    def usarHabilidadEspecial(self):
        print(f"{self.nombre} usa su habilidad especial de {self.clase}.")

class Enemigo(Personaje):
    def __init__(self, nombre: str, nivel: int, tipo: str):
        super().__init__(nombre, nivel)
        self.tipo = tipo

    def gritar(self):
        print(f"{self.tipo} grita por SPARTA.")
    

jugador = Jugador("Cardia", 10, "Mago")
jugador.atacar()
jugador.usarHabilidadEspecial()


enemigo = Enemigo("Orco Salvaje", 8, "Orco")
enemigo.atacar()
enemigo.gritar()