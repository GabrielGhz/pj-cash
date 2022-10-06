# número do cliente, número da conta e valor sacado

form={"nm":"",   #nome
    'rg':"",     #RG
    'cpf':"",    #CPF
    'dn':"",     #DataDeNascimento
    'end':""     #Endereço
}
#um novo valor vai ser adicionado aos valor vazio na chave do dicionário form
form['nm'] = input("Digite seu nome: ")
form['cpf'] = int(input("Digite seu CPF: "))
form['rg'] = int(input("Digite seu RG: "))
form['dn'] = input("Digite sua Data de nascimento: ")
form['end'] = input("Digite o endereço: ")

#aqui ira mostrar o Formulário final do Usuário
print('Seu nome é:', form['nm'],
'\nSeu Rg é:', form['rg'],
'\nE seu CPF é:', form['cpf'],
'\nSua data de nascimento é:', form['dn'],
'\nE seu endereço é:', form['end'])

meus_saques = {



}
