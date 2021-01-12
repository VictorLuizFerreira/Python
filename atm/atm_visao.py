'''
função que transforma uma variável
em uma mensagem(string) não pré definida,
para depois retornar a mesma
possibilitando o usuário digitar algo.
'''

def ask_string(message):
    v = input(message)
    return v

'''
função que transforma uma variável 
em uma mensagem de valor inteiro(int)
não pré definida,
para depois retornar a mesma,
possibilitando o usuário digitar algo
e, se caso ele coloque algo
que não seja um inteiro,
a função trata o erro com uma mensagem pré definida,
e retorna a mensagem de valor inteiro(int)
até que o usuário acerte.
'''

def ask_int(message, error_message = "not a int value"):
    try:
        v = int(input(message))
        return v
    except ValueError:
        print(error_message)
        return ask_int(message, error_message)

'''
função que transforma uma variável 
em uma mensagem de valor ponto flutuante(float)
não pré definida,
para depois retornar a mesma,
possibilitando o usuário digitar algo
e, se caso ele coloque algo
que não seja um float,
a função trata o erro com uma mensagem pré definida,
e retorna a mensagem de valor ponto flutuante(float)
até que o usuário acerte.
'''

def ask_float(message, error_message = "not a float value"):
    try:
        v = float(input(message))
        return v
    except ValueError:
        print(error_message)
        return ask_float(message, error_message)

'''
função que transforma uma variável 
nas opções que o atm possui(string),
para depois retornar a mesma,
possibilitando o usuário digitar
qual das opções ele deseja realizar.
'''

def showOptions():
    option = input("---------------------------\n" +
                      "1 - Sacar\n" +
                      "2 - Depositar\n" +
                      "3 - Extrato\n" +
                      "4 - Transferência\n" +
                      "0 - Sair\n\n" +
                      "Opção: ")
    return option