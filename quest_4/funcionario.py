# 4) Hierarquia de Funcionários. O departamento de RH de uma empresa precisa de um sistema que calcule o pagamento de seus funcionários. 
# A base de cálculo é a mesma para todos, mas gerentes e vendedores possuem bônus específicos.
# Desenvolva uma classe Funcionario com atributos nome e salario. Crie um método calcular_bonus() que, na classe base, simplesmente retorna o salário do funcionário. 
# Em seguida, crie a subclasse Gerente que, além dos atributos herdados, possui um atributo bonus_percentual.
# Sobrescreva o método calcular_bonus() para que ele retorne o salário acrescido do percentual de bônus.
# Escreva um script main.py para validar a implementação. Crie uma instância de Funcionario e uma de Gerente. 
# Para cada um, chame o método calcular_bonus() e exiba o resultado, confirmando que o cálculo para o gerente inclui o bônus.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus_percentual):
        super().__init__(nome, salario)
        self.bonus_percentual = bonus_percentual

    def calcular_bonus(self):
        return self.salario + (self.salario * self.bonus_percentual / 100)
    
    