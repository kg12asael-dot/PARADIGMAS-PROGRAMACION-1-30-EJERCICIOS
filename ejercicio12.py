class Video:
    def __init__(self, titulo: str, categoria: str, duracion: int):
        """
        Inicialización de los atributos de la clase
        """
        
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria

    def mirar_video(self):
        """
        Este método permite ver el video:
        Muestra en la consola la información relacionada con el video
        """
        print("Iniciando el video...")
        print(f"El video que estás viendo se titula '{self.titulo}' " +
              f"de la categoría '{self.categoria}' con una duración de {self.duracion} minutos.")

    def detener_video(self):
        """
        Este método permite detener el video
        """
        print("Deteniendo el video.")

class Audio:
    def __init__(self, nombre_artista: str, titulo: str):
        """
        Inicialización de los atributos
        """
        
        self.titulo = titulo
        
        self.nombre_artista = nombre_artista

    def escuchar_audio(self):
        """
        Este método permite escuchar el audio mostrando una cadena de caracteres en la consola y
        muestra la información relacionada con el audio
        """
        print("Iniciando el audio... ")
        print(f"El audio que estás escuchando es '{self.titulo}' producido \n"
              f"por el artista '{self.nombre_artista}'")

    def detener_audio(self):
        """
        Detener la reproducción del audio
        """
        print("Deteniendo la reproducción del audio.")


class Media(Video, Audio):
    """
    Herencia múltiple: Esta clase hereda de la clase Video y de la clase Audio al mismo tiempo
    """
    def __init__(self, titulo: str, categoria: str, duracion: int, nombre_artista: str):
        
        
        Video.__init__(self, titulo, categoria, duracion)
   
        Audio.__init__(self, nombre_artista, titulo)

media_1 = Media("Título 1", "infantil", 100, "Artista 1")

media_1.escuchar_audio()

media_1.mirar_video()

media_1.detener_audio()

media_1.detener_video()