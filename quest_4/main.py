from funcionario import Funcionario, Gerente

funcionario = Funcionario("Vitor", 3500.00)
gerente = Gerente("José", 5400.00, 30)


print(f"Funcionário: {funcionario.nome}, Pagamento: R${funcionario.calcular_bonus():.2f}")
print(f"Gerente: {gerente.nome}, Pagamento: R${gerente.calcular_bonus():.2f}")

