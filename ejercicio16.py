class ManipuladoresArchivos:
    def __init__(self, nombreArchivo: str):
        """
        constructor
        """
        self.nombreArchivo = nombreArchivo
        
        self.archivo = open(nombreArchivo, "r+") 
        print(f"El archivo '{nombreArchivo}' sido abierto en modo lectura y escritura!")

    def escribir_archivo(self, frase: str):
        """
        Este método permite escribir una frase en un archivo
        """
        self.archivo.write(frase)
        print(f"La frase '{frase}' ha sido escrita en el archivo {self.nombreArchivo}")

    def __del__(self):
        """
        Destructor: permite cerrar el archivo y eliminar las referencias de objetos
        vinculadas al objeto creado.
        """
        self.archivo.close()
        print(f"El archivo {self.nombreArchivo} ha sido cerrado.")


archivo_1 = ManipuladoresArchivos('archivo_prueba.txt')
archivo_1.escribir_archivo("Hola, ¿cómo estás?")

del archivo_1