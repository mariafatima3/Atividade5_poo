from produto import Produto, Eletronico

livro = Produto("Python Levado a Sério", 66.10)
smartphone = Eletronico("Samsung Galaxy M54", 2400.00, 12)

print("Livro".center(50))
livro.exibir_detalhes()

print("smartphone".center(50))
smartphone.exibir_detalhes()

