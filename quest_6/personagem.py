# 6)Personagens de um Jogo de RPG: Em um jogo de RPG, você precisa modelar diferentes classes de personagens. 
# Todos os personagens têm nome e nível, mas a forma como eles atacam varia. Crie uma classe Personagem com os atributos nome, nivel e um método atacar().
# O método atacar() da classe base deve retornar uma string como "{nome} realizou um ataque genérico." 
# Crie duas subclasses: Guerreiro, que possui um atributo extra arma, e Mago, com um atributo extra magia. 
# Sobrescreva o método atacar() em Guerreiro para retornar "{nome} atacou com sua arma {arma}!" e em Mago para retornar "{nome} lançou a magia {magia}!".
# Crie um arquivo main.py onde você instancia um Guerreiro e um Mago. 
# Para cada instância, chame o método atacar() e imprima o resultado, verificando que a mensagem de ataque é específica para cada classe.

class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        return f"{self.nome} realizou um ataque genérico."


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma

    def atacar(self):
        return f"{self.nome} atacou com sua arma {self.arma}!"


class Mago(Personagem):
    def __init__(self, nome, nivel, magia):
        super().__init__(nome, nivel)
        self.magia = magia

    def atacar(self):
        return f"{self.nome} lançou a magia {self.magia}!"
