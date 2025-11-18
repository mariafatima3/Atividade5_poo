# 5) Formas Geométricas: Você está criando uma ferramenta de desenho que precisa calcular a área de diferentes formas geométricas.
# A fórmula para cada forma é diferente, mas todas são "formas". Crie uma classe base com um método que lança um erro chamada Forma.
# Esta classe deve ter um método calcular_area(). Crie duas subclasses: Retangulo, com os atributos base e altura, e Circulo, com o atributo raio. 
# Implemente o método calcular_area() em cada uma das subclasses para que retorne a área correta de acordo com suas propriedades. 
# Para o círculo, considere usar 3.14 como valor de PI.

class Forma:
    def calcular_area(self):
        raise NotImplementedError("O método calcular_area() deve ser implementado nas subclasses.")

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura 

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio 
        
    def calcular_area(self):
         return 3.14 * (self.raio ** 2)
      
