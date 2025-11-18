# Supondo que as classes foram definidas em um arquivo chamado formas.py
from formas import Retangulo, Circulo

# Criando instâncias das formas
meu_retangulo = Retangulo(base=10, altura=5)
meu_circulo = Circulo(raio=4)

# Calculando e exibindo as áreas
area_retangulo = meu_retangulo.calcular_area()
area_circulo = meu_circulo.calcular_area()

print(f"A área do retângulo é: {area_retangulo}")
print(f"A área do círculo é: {area_circulo:.2f}")