import cliente
import random
print("Olá, seja Bem - vindo ao banco PJ CASH")
while True:
    p = int(input("Você deseja se cadastrar: \n 1-SIM \n 2-NÃO \n  "))
    if p == 2:
        print("OBRIGADO PELA VISITA!")
        break
    if p == 1:
        print("Preencha as informações abaixo: ")
        cliente.cadastramento()
