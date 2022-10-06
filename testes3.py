import cliente
import random
print("Olá, seja Bem - vindo ao banco PJ CASH")
print(" 1- Empréstimo \n 2- Fazer uma conta" )
p = int(input("Selecione a opção que você deseja: "))
if p == 2:
    print("Você precisa realizar um cadastro, selecione as informações a seguir: " )
    cadastro={
        "nm":"",
        'rg':"",
        'cpf':"",
        'dn':"",
        'end':"",
        'mn':""
    }  
    x = (random.randrange(0,9999999))
    cadastro['nm'] = input("Digite seu nome completo: ")
    cadastro['cpf'] = int(input("Digite seu CPF: "))
    cadastro['rg'] = int(input("Digite seu RG: "))
    cadastro['dn'] = input("Digite sua Data de nascimento: ")
    cadastro['end'] = input("Digite o endereço: ")
    cadastro["mn"] = x
    print("seu numero de cliente é: {}".format(x))
