# 8) Produtos de E-commerce: Em um site de e-commerce, todos os produtos têm nome e preço. 
# No entanto, produtos eletrônicos têm garantia, e essa informação precisa ser exibida na página do produto.
# Crie uma classe Produto com os atributos nome, preco e um método exibir_detalhes(). 
# Este método deve imprimir o nome e o preço do produto. Crie uma subclasse Eletronico que herda de Produto e adiciona um atributo tempo_garantia (em meses).
#  Sobrescreva o método exibir_detalhes() na classe Eletronico para que ele mostre também o tempo de garantia.
# Desenvolva um script main.py para testar suas classes. Nele, crie um objeto da classe Produto (ex: um livro) e um objeto da classe Eletronico (ex: um smartphone). 
# Chame o método exibir_detalhes() para ambos e confirme que a informação da garantia aparece apenas para o produto eletrônico.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def exibir_detalhes(self):
        print(f"nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
class Eletronico(Produto):
    def __init__(self, nome, preco, tempo_garantia):
        super().__init__(nome, preco)
        self.tempo_garantia = tempo_garantia

    def exibir_detalhes(self):
        print(f"nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Garantia: {self.tempo_garantia} meses")