# 2) Catálogo de Veículos: Uma concessionária precisa de um sistema para catalogar seu estoque. 
# Todos os veículos possuem uma marca e um modelo, mas carros e motos têm características específicas que precisam ser detalhadas.
# Crie uma classe Veiculo com os atributos marca e modelo, e um método detalhar(). Este método deve retornar uma string contendo a marca e o modelo do veículo. 
# Depois, crie duas subclasses: Carro, que deve ter um atributo adicional numero_portas, e Moto, com um atributo adicional tipo_partida (ex: "elétrica", "pedal"). 
# Sobrescreva o método detalhar() em ambas as subclasses para que a string de retorno inclua também seus atributos específicos.
# Crie um arquivo main.py para testar suas classes. Nele, instancie um objeto da classe Carro e um da classe Moto, preenchendo seus atributos. 
# Em seguida, chame o método detalhar() de cada objeto e imprima o resultado no console para verificar se as informações, 
# incluindo as específicas de cada subclasse, são exibidas corretamente.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalhar(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
class carro(Veiculo):
        def __init__(self, marca, modelo, numero_portas):
             super().__init__(marca, modelo)
             self.numero_portas = numero_portas
        
        def detalhar(self):
             return f"Marca: {self.modelo}. Numeros de portas:{self.numero_portas}"
        
class moto(Veiculo):
     def __init__(self, elétrica, pedal, tipo_partida):
         super().__init__(elétrica, pedal)
         self.tipo_partida = tipo_partida

     def detalhar(self):
          return f"Modelo: {self.modelo}, Tipo de partida: {self.tipo_partida} "