# número do cliente, número da conta corrente e o saldo
def conta_corrente():
    print("Você deseja fazer uma conta? \n 1-SIM  ou 2- NÃO \n  ")
    p1 = int(input("Digite o número correspondente: "))
    if p1 == 2:
        print('ok')
    elif p1 == 1:
        nome= input("Digite seu nome completo: ")
        cpf = int(input("Digite seu CPF: "))
        end = input("Digite seu endereço: ")
        email = input("Digite seu e-mail: ")
        num = int(input("Digite seu número de telefone: "))
        print("Sua conta foi criada")
    elif p1 != 0 and 1:
        print("Número inválido")

conta_corrente()   

