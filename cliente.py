# vai receber o cadastro dos clientes
import random

def cadastramento():
    cadastro={
        "nm":"",
        'rg':"",
        'cpf':"",
        'dn':"",
        'end':"",
        'mn':"",
        'tel':""
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
    while True:
        tel = input("Digite o numero do seu telefone celular: ")
        if str.isdigit (tel) == True:
            break
        else:
            print("Por favor, digite somente NÚMEROS")
            continue
    dn = input("Digite sua Data de nascimento: ")
    cpf = int(cpf)
    rg = int(rg)
    tel = int(tel)
    mn = x
    cadastro['nm'] = nm
    cadastro['cpf'] = cpf
    cadastro['rg'] = rg
    cadastro['dn'] = dn
    cadastro['end'] = end
    cadastro['tel'] = tel
    cadastro["mn"] = mn
    print("")
    print("cadastrado com sucesso! \n")
    print("seu numero de cliente é: {} \n".format(x))
cadastramento()