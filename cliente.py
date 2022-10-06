# vai receber o cadastro dos clientes

import random
from timeit import repeat

def cadastramento():
    cadastro={
        "nm":"",
        'rg':"",
        'cpf':"",
        'dn':"",
        'end':"",
        'mn':""
    }
    x = (random.randrange(0,9999999))
    cadastro['nm'] = str(input("Digite seu nome completo: "))
    cadastro['cpf'] = int(input("Digite seu CPF: "))
    cadastro['rg'] = int(input("Digite seu RG: "))
    cadastro['dn'] = str(input("Digite sua Data de nascimento: "))
    cadastro['end'] = str(input("Digite o endereço: "))
    cadastro["mn"] = x

    print("cadastrado com sucesso!")
    print("seu numero de cliente é: {}".format(x))
