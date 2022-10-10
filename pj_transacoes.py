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
    try:
        cad = int(input("Você deseja se cadastrar: \n1-SIM \n2-NAO \n:"))
        if cad == 2:
            while True:
                dep = int(input("Você gostaria de fazer um deposito? \n1-SIM \n2-NAO \n"))
                if dep == 1:
                    print("Depositado com sucesso! ")
                    break
                if dep == 2:
                    print("OBRIGADO PELA VISITA!")
                    break
                elif dep != 2 or dep != 1:
                    print("Por favor, digitar somente os numeros pedidos!")
                    continue
            break    
        if cad == 1:
            print("Preencha as informações abaixo: ")
            cliente.cadastramento()
            while True:
                cc = int(input("Voce deseja criar uma conta corrente? \n1-SIM \n2-NAO \n:"))
                if cc == 2:
                    for x in range(9999):
                        while True:
                            dep = int(input("Você deseja realizar um deposito? \n1-SIM \n2-NAO \n:"))                    
                            if dep == 2:
                                while True:
                                    empr = int(input("Você deseja realizar um emprestimo? \n1-SIM \n2-NAO \n:"))
                                    if empr == 2:
                                        break
                                    if empr == 1:
                                        print('funcao emprestimo')
                                        break
                                    elif empr != 1 or empr != 2:
                                        print("Por favor, digitar somente os numeros pedidos!")
                                        continue
                                break    
                            if dep == 1:
                                print('funcao deposito')
                                print("depositado com sucesso")
                                continue
                            elif dep != 1 or dep != 2:
                                print("Por favor, digitar somente os numeros pedidos!")
                                continue
                        break    
                    break
                if cc == 1:
                    print("Preencha as informações abaixo: ")
                    print("preenchido com sucesso!")
                    break
                elif cc != 1 or cc != 2:
                    print("Por favor, digitar somente os numeros pedidos!")
                    continue 
        elif cad != 1 or cad != 2:
            print("Por favor, digitar somente os numeros pedidos!")
            continue    
    except ValueError:
        print("Por favor, digitar somente numeros nessa seção! \n \nA toda seção foi reiniciada! \n")
    while True:
        try:
            for x in range(9999):
                dep = int(input("Você deseja depositar, sacar ou nenhuma das anteriores?: \n1-depositar \n2-sacar \n3-nenhuma das anteriores \n: "))
                if dep == 1:
                    print('funcao depositar')
                    print('depositado com sucesso')
                    continue
                elif dep == 2:
                    print('funcao sacar')
                    print('informações de saque')
                    continue
                elif dep == 3:
                    print("Obrigado pela visita!")
                    break
                elif dep != 3 or dep != 2 or dep != 1:
                    print("por favor, digite os numeros inseridos")
                    continue
            break    
        except ValueError:
            print("Por favor, digitar somente numeros nessa seção! \n \nA toda seção foi reiniciada! \n")
    break