# 7) Postagens em uma Rede Social: Imagine o feed de uma rede social. Nele, podem aparecer postagens de texto e postagens com fotos. 
# Ambas são postagens, mas a forma de exibição é ligeiramente diferente.
# Crie uma classe Post com um atributo texto e um método exibir() que imprime o texto da postagem. 
# Em seguida, crie a subclasse FotoPost que, além do texto, tem um atributo url_imagem. 
# Sobrescreva o método exibir() para que ele imprima o texto e, em seguida, uma representação da imagem, como "[Imagem em {url_imagem}]".

class Post:
    def __init__(self, texto):
        self.texto = texto 

    def exibir(self):
        print(self.texto) 


class FotoPost(Post):
    def __init__(self, texto, url_imagem):
        super().__init__(texto) 
        self.url_imagem = url_imagem 

    def exibir(self):
      
        print(self.texto)
        print(f"[Imagem em {self.url_imagem}]")


