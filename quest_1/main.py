from zoo import Cachorro, Gato, Vaca


rex = Cachorro("Rex")
felix = Gato("Félix")
mimosa = Vaca("Mimosa")


animais = [rex, felix, mimosa]


print("Sons do zoológico virtual:")
for animal in animais:
    print(f"{animal.nome} diz: ", end="")
    animal.emitir_som()