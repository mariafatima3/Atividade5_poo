# 1) O Zoológico Virtual. Imagine que você está desenvolvendo um software para um zoológico virtual.
# O sistema precisa ser capaz de representar diferentes animais e os sons que eles fazem.
# Crie uma classe base chamada Animal que possua um método emitir_som().
# Este método, na classe base, pode simplesmente imprimir uma mensagem genérica como "O animal emitiu um som".
# Em seguida, crie três classes que herdam de Animal: Cachorro, Gato e Vaca.
# Em cada uma dessas subclasses, sobrescreva o método emitir_som() para que ele imprima o som característico do respectivo animal ("Au au!", "Miau!", "Muuu!").


class Animal:
    def __init__(self,nome):
        self.nome = nome


    def emitir_som(self):
        print("O animal emitiu um som.")


class Cachorro(Animal):
     def emitir_som(self):
         print("Au au!")


class Gato(Animal):
     def emitir_som(self):
        print("Miau!")


class Vaca(Animal):
     def emitir_som(self):
        print("Muuu!")