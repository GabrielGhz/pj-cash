# vai receber o cadastro dos clientes
import random

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
    while True:
        nm = input("Digite seu nome completo: ")
        if str.isdigit (nm) == False:
            break
        else:
            print("Por favor, digite somente LETRAS")
            continue
    while True:
        cpf = input("Digite seu CPF: ")
        if str.isdigit (cpf) == True:
            break
        else:
            print("Por favor, digite somente NÚMEROS")
            continue
    while True:
        rg = input("Digite seu RG: ")
        if str.isdigit (rg) == True:
            break
        else:
            print("Por favor, digite somente NÚMEROS")
            continue
    while True:
        end = input("Digite o endereço: ")
        if str.isdigit (end) == False:
            break
        else:
            print("Por favor, digite somente LETRAS")
            continue
    dn = input("Digite sua Data de nascimento: ")
    cpf = int(cpf)
    rg = int(rg)
    mn = x
    cadastro['nm'] = nm
    cadastro['cpf'] = cpf
    cadastro['rg'] = rg
    cadastro['dn'] = dn
    cadastro['end'] = end
    cadastro["mn"] = mn

    print("cadastrado com sucesso!")
    print("seu numero de cliente é: {}".format(x))