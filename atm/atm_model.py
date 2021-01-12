accounts = {"AX476T": ["José Renato Martins", "007.008.009-00", 23.56],
            "BF896T": ["Bolsonaro", "007.007.007-77", 2847233.56],
            "BATMAN": ["Batman", "000.000.000-01", 1000.56],
            "AXXX67": ["Iron Man", "123.007.007-77", -522324341.56]}

'''
função que checa a identidade do usuário
no dicionário criado,e se der erro de chaves,
ele trata, retornando um booleano.
'''


def check_id(identity):
    try:
        accounts[identity]
    except KeyError:
        return False
    return True


'''
função que realiza o saque no atm,
aonde, se a identidade não for válida,
ele sai, e se for válida, a função vai no dicionário,
na chave do usuário, na posição 2,
e subtrai o valor que está na conta(posição 2 do dicionário),
com o que ele digitou,
continuando o programa.
'''


def perform_withdraw(identity, value):
    if not check_id(identity):
        return False
    accounts[identity][2] -= value
    return True


'''
função que realiza o depósito no atm,
aonde, se a identidade não for válida,
ele sai, e se for válida, a função vai no dicionário,
na chave do usuário, na posição 2,
e soma o valor que está na conta(posição 2 do dicionário),
com o que ele digitou,
continuando o programa.
'''


def perform_deposit(identity, value):
    if not check_id(identity):
        return False
    accounts[identity][2] += value
    return True


'''
função que realiza a transferência no atm,
aonde, se as duas identidades, tanto a do usuário
presente quanto a de quem ele for transferir, forem válidas,
a função vai no dicionário,
na chave do usuário, na posição 2,
e subtrai o valor que
está na conta(posição 2 do dicionário),
com o que ele digitou,
e soma esse valor com o valor que
está na conta(posição 2 do dicionário) de quem ele quer transferir,
com o que ele digitou,
continuando o programa.
'''


def perform_transfer(identity, identity_dep, value):
    if check_id(identity) and check_id(identity_dep):
        accounts[identity][2] -= value
        accounts[identity_dep][2] += value
        return True
    return False
