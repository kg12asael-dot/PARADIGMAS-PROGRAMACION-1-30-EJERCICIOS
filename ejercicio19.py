class Texto:
    def __init__(self, frase: str):
        """
        Constructor que permite inicializar el atributo
        'frase'.
        """
        self.frase = frase

    def mostrar_texto(self):
        """
        Este método permite mostrar la 'frase'
        en la consola.
        """
        print(self.frase)

class TextoItalico(Texto):
    def __init__(self, frase: str):
        """
        Constructor
        """
        super().__init__(frase)

    def mostrar_texto(self):
        """
        Este método permite mostrar el texto en la consola en Itálica.
        Para indicar que una frase está en itálica, añadimos un guion
        bajo al principio y al final de la frase.
        """
        print("_" + self.frase + "_")

class TextoNegrita(Texto):
    def __init__(self, frase: str):
        """
        Constructor
        """
        super().__init__(frase)

    def mostrar_texto(self):
        """
        Este método permite mostrar el texto en la consola en Negrita.
        Para indicar que una frase está en negrita, añadimos un doble asterisco
        al principio y al final de la frase.
        """
        print("**" + self.frase + "**")

texto_1 = Texto("Aprender POO en Python a través de la práctica")
texto_2 = TextoItalico("Aprender POO en Python a través de la práctica")
texto_3 = TextoNegrita("Aprender POO en Python a través de la práctica")


textos = [texto_1, texto_2, texto_3]


for texto in textos:
    texto.mostrar_texto()