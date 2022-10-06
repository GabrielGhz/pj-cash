from cliente import cadastramento
import random

# import cliente
# import conta_corrente
# import minhas_transferencias
# import meus_depositos
# import meus_saques
# import meus_emprestimos

# todas as funções referentes ao banco (empréstimo, depósito e saque)
print("Olá, seja Bem - vindo ao banco PJ CASH")
while True:
    p = int(input("Você deseja se cadastrar: \n 1-SIM \n 2-NÃO \n  "))
    if p == 2:
        print("OBRIGADO PELA VISITA!")
        break
    if p == 1:
        print("Preencha as informações abaixo: ")
        cadastramento()