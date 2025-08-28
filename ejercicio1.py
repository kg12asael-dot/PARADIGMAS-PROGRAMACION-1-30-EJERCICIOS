class Galleta:
    def __init__(self,nombre,forma):
        self.nombre=nombre
        self.forma=forma
    def hornear(self):
        print(f"Esta gelleta con {self.nombre} ha sido horneada en forma de {self.forma} Buen provecho!!")
        
galleta_1=Galleta("chispas de chocolate","estrella")
galleta_1.hornear()