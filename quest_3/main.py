from midia import Audio, Video

musica_favorita = Audio("Bohemian Rhapsody", "Queen")
filme_favorito = Video("Interestelar", "4K")


playlist = [musica_favorita, filme_favorito]


for item in playlist:
    item.reproduzir()

