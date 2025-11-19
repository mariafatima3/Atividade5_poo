from veiculos import Carro, Moto

carro1 = Carro("BYD", "BYD Dolphin", 4)
carro2 = Carro("Toyota", "sedã Corolla", 4)
moto1 = Moto("Honda", "CG 125FAN KS ", "partida")
moto2 = Moto("Watts", "W125", "eletrica")

print(" Carro 1".center(25))
print(carro1.detalhar())

print("\n   Carro 2".center(50))
print(carro2.detalhar())

print("\n   Moto 1".center(50))
print(moto1.detalhar())

print(" \n   Moto 2 ".center(50))
print(moto2.detalhar())



