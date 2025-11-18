from social import Post, FotoPost

# Criando postagens de diferentes tipos
post_texto = Post("Que dia excelente para programar em Python!")
post_foto = FotoPost("Olha o meu novo setup de trabalho!", "[https://example.com/minha-foto.jpg](https://example.com/minha-foto.jpg)")

# Adicionando ao feed
feed = [post_texto, post_foto]

# Exibindo o feed
for postagem in feed:
    postagem.exibir()
    print("-" * 30)


