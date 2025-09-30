class Galleta:
    def __init__(self, nombre, forma):
        self.nombre=nombre
        self.forma=forma
        
    def hornear(self):
        print("Esta", self.nombre, "horneada en forma de", self.forma)
        print("Buen provecho :)")
        
galleta_1=Galleta("galleta con chispas de chocolate", "estrella.")
galleta_1.hornear()
              
        