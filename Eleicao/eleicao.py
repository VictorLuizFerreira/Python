import os

candidates_pres = {19: "Alvaro Dias", 24: "Ciro Gomes",
                   45: "Geraldo Alckmin", 21: "Jair Bolsonaro",
                   42: "Marina Silva", 13: "Lula",
                   29: "PSTU", 0: "Nulo"}

candidates_gover = {12: "Paulo Chagas", 10: "Leo Stronda",
                    31: "Rogério Rosso", 22: "Bruno Gianerinni",
                    97: "Nando Moura", 0: "Nulo"}

candidates_sen = {67: "Paulo Guina", 14: "João Vargas", 26: "Bruno Marão",
                  88: "Wal do Açaí", 91: "Amanda Nudes", 51: "Molusco Cachaceiro",
                  87: "Ninja", 69: "Malakoi", 0: "Nulo"}

votes_pres = {19: 0, 24: 0,
              45: 0, 21: 0,
              42: 0, 13: 0,
              29: 0, 0: 0}

votes_gover = {12: 0, 10: 0,
               31: 0, 22: 0,
               97: 0, 0: 0}

votes_sen1 = {67: 0, 14: 0,
              26: 0, 88: 0,
              91: 0, 51: 0,
              87: 0, 69: 0,
              0: 0}

votes_sen2 = {67: 0, 14: 0,
              26: 0, 88: 0,
              91: 0, 51: 0,
              87: 0, 69: 0,
              0: 0}

election = True

while election:

    choice = int(input("---------------------------------\n" +
                       "1. Para votar\n" +
                       "2. Para sair\n" +
                       "---------------------------------\n" +
                       "Opção: "))
    if choice == 1:

        num_pres = input("Informe o número do seu candidato a presidência: ")

        try:
            num_pres = int(num_pres)

            print("O candidato á presidência escolhido foi: ", candidates_pres[num_pres])

            votes_pres[num_pres] += 1



        except (ValueError, KeyError) as a:
            confirmation = input("Você irá anular seu voto. Confirma? (S/N): ")
            if confirmation.upper() == "S":
                print("Voto anulado.")
                votes_pres[0] += 1

        num_gover = input("Informe o número do seu candidato a governador(a): ")

        try:
            num_gover = int(num_gover)

            print("O candidato á governador(a) escolhido foi: ", candidates_gover[num_gover])

            votes_gover[num_gover] += 1


        except (ValueError, KeyError) as a:
            confirmation = input("Você irá anular seu voto. Confirma? (S/N): ")
            if confirmation.upper() == "S":
                print("Voto anulado.")
                votes_gover[0] += 1

        num_sen1 = input("Informe o número do seu 1º candidato a senador(a): ")
        num_sen2 = input("Informe o número do seu 2º candidato a senador(a): ")

        try:
            num_sen1 = int(num_sen1)
            num_sen2 = int(num_sen2)

            print("O 1º candidato á senador(a) escolhido foi: ", candidates_sen[num_sen1])
            print("O 2º candidato á senador(a) escolhido foi: ", candidates_sen[num_sen2])
            votes_sen1[num_sen1] += 1
            votes_sen2[num_sen2] += 1


        except (ValueError, KeyError) or num_sen2 == num_sen1 as a:
            confirmation = input("Você irá anular seu voto. Confirma? (S/N): ")
            if confirmation.upper() == "S":
                print("Voto anulado.")

                votes_sen1[0] += 1
                votes_sen2[0] += 1


    elif choice == 2:
        election = False

    else:
        print("Masss que burrrooo! Escolha um Número Válido.")

os.system("clear")
print("\n~~Resultado da eleição~~\n ")

print("Candidatos a presidência:\n")

for key in candidates_pres:
    print(candidates_pres[key] + " : " + str(votes_pres[key]))
ganhador_pres = max(votes_pres, key=votes_pres.get)
print('O ganhador da eleição para presidência foi: ', candidates_pres[ganhador_pres])

print("\nCandidatos a governador(a):\n")

for key in candidates_gover:
    print(candidates_gover[key] + " : " + str(votes_gover[key]))
ganhador_gover = max(votes_gover, key=votes_gover.get)
print('O ganhador da eleição para governador(a) foi: ', candidates_gover[ganhador_gover])

print("\nCandidatos a senador(a):\n")

for key in candidates_sen:
    print(candidates_sen[key] + " : " + str(votes_sen1[key]))
ganhador_sen1 = max(votes_sen1, key=votes_sen1.get)
print('O 1º ganhador da eleição para senador(a) foi: ', candidates_sen[ganhador_sen1])

print("\nCandidatos a senador(a):\n")

for key in candidates_sen:
    print(candidates_sen[key] + " : " + str(votes_sen2[key]))
ganhador_sen2 = max(votes_sen2, key=votes_sen2.get)
print('O 2º ganhador da eleição para senador(a) foi: ', candidates_sen[ganhador_sen2])






