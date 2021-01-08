import random

banca = 100000.00

roulette_board = {0: ["green", "none", "none", "none"],
                  1: ["black", "first", "first-half", "odd"],
                  2: ["red", "first", "first-half", "even"],
                  3: ["black", "first", "first-half", "odd"],
                  4: ["red", "first", "first-half", "even"],
                  5: ["black", "first", "first-half", "odd"],
                  6: ["red", "first", "first-half", "even"],
                  7: ["black", "first", "first-half", "odd"],
                  8: ["red", "first", "first-half", "even"],
                  9: ["black", "first", "first-half", "odd"],
                  10: ["red", "first", "first-half", "even"],
                  11: ["black", "first", "first-half", "odd"],
                  12: ["red", "first", "first-half", "even"],
                  13: ["black", "second", "first-half", "odd"],
                  14: ["red", "second", "first-half", "even"],
                  15: ["black", "second", "first-half", "odd"],
                  16: ["red", "second", "first-half", "even"],
                  17: ["black", "second", "first-half", "odd"],
                  18: ["red", "second", "first-half", "even"],
                  19: ["black", "second", "second-half", "odd"],
                  20: ["red", "second", "second-half", "even"],
                  21: ["black", "second", "second-half", "odd"],
                  22: ["red", "second", "second-half", "even"],
                  23: ["black", "second", "second-half", "odd"],
                  24: ["red", "second", "second-half", "even"],
                  25: ["black", "third", "second-half", "odd"],
                  26: ["red", "third", "second-half", "even"],
                  27: ["black", "third", "second-half", "odd"],
                  28: ["red", "third", "second-half", "even"],
                  29: ["black", "third", "second-half", "odd"],
                  30: ["red", "third", "second-half", "even"],
                  31: ["black", "third", "second-half", "odd"],
                  32: ["red", "third", "second-half", "even"],
                  33: ["black", "third", "second-half", "odd"],
                  34: ["red", "third", "second-half", "even"],
                  35: ["black", "third", "second-half", "odd"],
                  36: ["red", "third", "second-half", "even"]}


def ap_val(x, z="Erro"):
    try:
        a = int(input(x))
        roulette_board[a]
        return a
    except(ValueError, KeyError) as a:
        print(z)
        return ap_val(x)


bet_val = ap_val("Casa apostada: ")


def val_ap(y, z="Erro"):
    try:
        b = float(input(y))
        return b
    except(ValueError) as a:
        print(z)
        return val_ap(y)


get_val = val_ap("Valor apostado: ")

casa_sort = random.choice(list(roulette_board.keys()))


def win_los(casa, aposta):
    if casa == casa_sort:
        aposta = banca - aposta
        print("Você ganhou!")
        return aposta
    else:
        aposta = banca + aposta
        print("Você perdeu!")
        return aposta


print("O número sorteado foi: ", casa_sort)
print("A casa ficou com: R$", win_los(bet_val, get_val))


def check_color(value, color):
    try:
        return roulette_board[value][0] == color
    except KeyError:
        return "ERRO DE TABULEIRO"


def check_terco(value, terco):
    try:
        return roulette_board[value][1] == terco
    except KeyError:
        return "ERRO DE TABULEIRO"


def check_half(value, half):
    try:
        return roulette_board[value][2] == half
    except KeyError:
        return "ERRO DE TABULEIRO"


def check_parity(value, parity):
    try:
        return roulette_board[value][3] == parity
    except KeyError:
        return "ERRO DE TABULEIRO"


def is_red(value):
    return check_color(value, "red")


def is_black(value):
    return check_color(value, "black")


def is_green(value):
    return check_color(value, "green")


def is_first(value):
    return check_terco(value, "first")


def is_second(value):
    return check_terco(value, "second")


def is_third(value):
    return check_terco(value, "third")


def is_n_part(value):
    return check_terco(value, "none")


def is_f_half(value):
    return check_half(value, "first-half")


def is_s_half(value):
    return check_half(value, "second-half")


def is_n_half(value):
    return check_half(value, "none")


def is_even(value):
    return check_parity(value, "even")


def is_odd(value):
    return check_parity(value, "odd")


def is_n_parity(value):
    return check_parity(value, "none")








