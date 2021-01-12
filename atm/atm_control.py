from OldCodes.atm.atm_visao import *
from OldCodes.atm.atm_model import *

'''
função que pede um valor inteiro(int),
o valor que será sacado,
ao usuário e se caso não estiver de acordo
com as funções de saque,
apareça uma mensagem de erro.
'''


def withdraw(identity):
    value = ask_int("Valor do saque: ")
    if not perform_withdraw(identity, value):
        print("Saque não pode ser realizado!")
        return
    print("Saque realizado com sucesso.\n" +
          "Verifique se realmente recebeu R$" + str(value))


'''
função que pede um valor inteiro(int),
o valor que será depositado,
ao usuário e se caso não estiver de acordo
com as funções de depósito,
apareça uma mensagem de erro.
'''


def deposit(identity):
    value = ask_int("Valor do deposito: ")
    if not perform_deposit(identity, value):
        print("deposito não pode ser realizado!")
        return
    print("deposito realizado com sucesso.\n" +
          "Verifique se realmente foi depositado R$" + str(value))


'''
função que mostra o extrato
do usuário através de sua identidade
no dicionário, na posição 2 do mesmo.
'''


def extract(identity):
    print("Seu saldo atual é: " + str(accounts[identity][2]))


'''
função que pede um valor inteiro(int),
o valor que será transferido,
e pede a conta que será realizada a transferência
ao usuário, e se caso não estiver de acordo
com as funções de transferência,
apareça uma mensagem de erro.
'''


def transfer(identity):
    value = ask_int("Valor da transferência: ")
    conta = ask_string("Conta: ")
    if not perform_transfer(identity, conta, value):
        print("Transferencia não pode ser efetuada!")
        return
    print("Transferência efetuada com sucesso para a conta: " + str(conta))


'''
função que termina com todo o programa
através de um exit, imprimindo uma string
e o nome do usuário.
'''


def close(identity):
    print("Bye Bye! Mr. " + accounts[identity][0])
    exit()


functions = {"1": withdraw, "2": deposit, "3": extract, "4": transfer, "0": close}

'''
função que pede para o usuário se identificar,
caso ele esteja no dicionário,
vai aparecer as opções do atm,
se ele não estiver, aparecerá uma mensagem de erro
e o programa será finalizado.
nas opções do atm,
sempre que o usuário estiver logado,
o programa não ira parar de rodar,
até que o usuário queira,
fazendo assim uma estrutura de repetção.
'''


def start():
    identity = ask_string("ID: ")
    valid = check_id(identity)
    if not valid:
        print("ERRO. USUÁRIIO NÃO IDENTIFICADO")
        return
    option = "enter"
    while option != "0":
        option = showOptions()
        functions[option](identity)


start()