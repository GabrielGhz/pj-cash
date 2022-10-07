import cliente
import random

# import cliente
# import conta_corrente
# import minhas_transferencias
# import meus_depositos
# import meus_saques
# import meus_emprestimos

# todas as funções referentes ao banco (empréstimo, depósito e saque)
import cliente
import random

print("Olá, seja Bem - vindo ao banco PJ CASH")
while True:
    cad = int(input("Você deseja se cadastrar: \n1-SIM \n2-NAO \n:"))
    if cad == 2:
        print("OBRIGADO PELA VISITA!")
        break
    if cad == 1:
        print("Preencha as informações abaixo: ")
        cliente.cadastramento()
    cc = int(input("Voce deseja criar uma conta corrente? \n1-SIM \n2-NAO \n:"))
    if cc == 2:
        for x in range(9999):
            dep = int(input("Você deseja realizar um deposito? \n1-SIM \n2-NAO \n:"))
            if dep == 2:
                empr = int(input("Você deseja realizar um emprestimo? \n1-SIM \n2-NAO \n:"))
                if empr == 2:
                    break
                if empr == 1:
                    print('funcao emprestimo')                    
                break
            if dep == 1:
                print('funcao deposito')
    if cc == 1:
        print("Preencha as informações abaixo: ")
        input("INFORMAÇÔES TESTE")
    dep = int(input("Você deseja depositar, sacar ou nenhuma das anteriores?: \n1-depositar \n2-sacar \n3-nenhuma das anteriores \n:"))    
    if dep == 1:
        print('funcao depositar')
    elif dep == 2:
        print('funcao sacar')
    else:
        break
