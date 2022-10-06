import cliente
# import conta_corrente
# import minhas_transferencias
# import meus_depositos
# import meus_saques
# import meus_emprestimos

# todas as funções referentes ao banco (empréstimo, depósito e saque)

while True:
    print('Olá, seja bem-vindo ao banco PJ Cash!')
    cadastrar_cliente = input('Deseja cadastrar um cliente? [s/N]\n').lower()
    if cadastrar_cliente == 's':
        cliente.cadastrar()
    elif cadastrar_cliente == 'n':
        print('algumacoisa algumacoisa não')
    else:
        print('Valor inválido')

    cadastrar_conta = input('Deseja cadastrar um conta corrente? [sim/não]\n').lower()
    # if cadastrar_conta == :

    # fazer_deposito
    break
