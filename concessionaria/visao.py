from OldCodes.concessionaria.veiculo import Vehicle


def obj(marc, nom, an, co, tip):
    val1 = True

    while val1:
        marca = input(marc)
        if marca == "":

            print("Digite uma data válida!")

        else:
            val1 = False

    val2 = True

    while val2:
        nome = input(nom)
        if nome == "":

            print("Digite um nome válido!")

        else:
            val2 = False

    val3 = True

    while val3:
        try:

            ano = int(input(an))

        except ValueError:

            print("Opa! Isso não é um ano!")

            continue

        if (ano < 1900 or ano > 2025):

            print("Digite uma data válida!")

        else:

            val3 = False

    val4 = True

    while val4:
        cor = input(co)
        if cor == "":

            print("Digite uma cor válida!")

        else:
            val4 = False

    val5 = True

    while val5:
        tipo = input(tip)
        if tipo == "":

            print("Digite um tipo válido!")

        else:
            val5 = False

    v = Vehicle(marca, nome, ano, cor, tipo)

    stri = v.to_file_string()

    return stri

