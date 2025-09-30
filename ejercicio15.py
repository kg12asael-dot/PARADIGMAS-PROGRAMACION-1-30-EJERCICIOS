class Empleado:
    def __init__(self, nombre: str, edad: int):
        """
        Constructor: Permite inicializar instancias de una clase
        """
        self.nombre = nombre
        self.edad = edad
        print(f"¡El empleado llamado {nombre} y de {edad} años ha sido creado!")

    def __del__(self):
        """
        Destructor: Permite eliminar las referencias del objeto
        """
        print(f"El destructor ha sido llamado, el empleado llamado {self.nombre} ha sido eliminado!")

empleado_1 = Empleado("Martin", 26)
empleado_2 = Empleado("Julien", 24)

del empleado_1
del empleado_2