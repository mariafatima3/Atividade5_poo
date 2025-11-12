# 3) Reprodutor de Mídia Você está desenvolvendo um reprodutor de mídias que pode tocar tanto arquivos de áudio quanto de vídeo. 
# Ambos são "arquivos", mas a forma de reproduzi-los contém informações diferentes.
# Crie uma classe Arquivo com um atributo nome e um método reproduzir() que imprime uma mensagem genérica como "Reproduzindo arquivo: {nome}". 
# Crie duas subclasses: Audio, com um atributo adicional artista, e Video, com um atributo resolucao. 
# Sobrescreva o método reproduzir() em Audio para imprimir "Tocando a música '{nome}' de {artista}" e em Video para imprimir "Exibindo o vídeo '{nome}' em {resolucao}".

class Arquivo:
    def __init__(self, nome):
        self.nome = nome
    
    def reproduzir(self):
        print(f"Reproduzindo arquivo: {self.nome}")

class Audio(Arquivo):
    def __init__(self, nome, artista):
        super().__init__(nome)
        self.artista = artista

    def reproduzir(self):
        print(f"Tocando a música '{self.nome}' de {self.artista}")

class  Video(Arquivo):
    def __init__(self, nome, resolucao):
        super().__init__(nome)
        self.resolucao = resolucao
    def reproduzir(self):
       print(f"Exibindo o vídeo '{self.nome}' em {self.resolucao}")
        

                