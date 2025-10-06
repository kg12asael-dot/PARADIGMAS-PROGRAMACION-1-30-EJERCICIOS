class GameList:
    def __init__(self):
        self.games = [
            "Dark Soul",
            "Demon Soul",
            "Ghost of Tsushima",
            "Halo",
            "God of War",
            "Hades",
            "Minecraft"
        ]

    def save_to_file(self, filename="games.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for game in self.games:
                file.write(game + "\n")

if __name__ == "__main__":
    lista = GameList()
    lista.save_to_file()
    print("Archivo 'games.txt' creado con éxito.")