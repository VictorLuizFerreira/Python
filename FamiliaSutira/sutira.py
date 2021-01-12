# 0

familias = {"acima de 80": ["Família Mariva", "Família Moreira"],
            "abaixo de 80": ["Família Mortana"]}

print("As famílias que possuem um nível de rivalidade acima de 80% são:\n\n",
      familias["acima de 80"], "\n")

# 1

inseto = {"carne": ["Chenpolin", "Otemti" "\n Milherta"],
          "sucção": ["Retrombis", "Chumelho"],
          "planta": ["Chumelho" "\n Vivider", "Alteris-Funchis" "\n Milherta"]}

tipo_alimentaçao = True

while tipo_alimentaçao:

    alimentaçao = input("Esse inseto se alimenta de carne, planta ou atravez de sucção?")

    if alimentaçao == "carne" or alimentaçao == "sucção" or alimentaçao == "planta":
        print("\nOs insetos que se alimentam de/por " + str(alimentaçao) + " são os:\n\n",
              inseto[alimentaçao][0], "\n",
              inseto[alimentaçao][1])
        tipo_alimentaçao = False

    else:
        print("\nPorfavor, digite uma alimentação válida!\n")

# 2

fam_inseto = {"Mortana": ["Chenpolin", "Retrombis", "Chumelho", "Otemti" "\n Milherta"],
              "Mariva": ["Retrombis", "Chumelho", "Vivider", "Alteris-Funchis"],
              "Moreira": ["Retrombis", "Chumelho", "Vivider", "Alteris-Funchis"]}

fam_verdadeira = True
while fam_verdadeira:
    family = input("\nVocê deseja saber da família Mortana, Mariva ou Moreira?")

    if family == "Mortana" or family == "Mariva" or family == "Moreira":
        print("\nA família " + str(family) + " conhece os insetos: \n\n",
              fam_inseto[family][0], "\n",
              fam_inseto[family][1], "\n",
              fam_inseto[family][2], "\n",
              fam_inseto[family][3], "\n")

        fam_verdadeira = False
    else:
        print("\nPorfavor, digite uma família válida!")

# 3

contador = 4
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVXZ"
carta_original = "AOPUIKO LKVNAO.RKXAO JUK XKILUNPEHDUI.OAI RKXAO RAJXANAIKO.QI ZEU ENUK AJPAJZAN. UOO. III"
carta_descriptografada = ""
for letra in carta_original:
    if letra == " " or letra == ".":
        carta_descriptografada = carta_descriptografada + letra
    else:
        posiçao = alfabeto.find(letra)
        posiçao_descriptografada = (posiçao + contador) % 24
        carta_descriptografada = carta_descriptografada + alfabeto[posiçao_descriptografada]
print("A carta deixada foi descriptografada e contia as seguintes informações:\n\n", carta_descriptografada)

# 4

'''
A família Mortana, por ter apenas criação de animais, facilita a proliferação de insetos carnívoros,
porem, ela tem uma porcentagem de rivalidade menor do que as outras.
Já as famílias Mariva e Moreira, possuem somente gãos e/ou cereais, com uma proliferação de insetos
que só comem plantas ou se alimentam por sucção, entretanto, as duas famílias possuem um nível de rivalidade bem alto.
Conclusão do caso:
As 3 famílias tem culpa, como dita a assinatura na carta com os MMM(3M).
As famílias Mariva e Moreira, por não possuirem nenhuma atividade com animal e
consequentemente não ter uma espécie de inseto carnívoro, convenceram a família Mortana
a fazer uma parceria para acabar com a fazenda Sutira, juntando todos os insetos para um unico objetivo.
'''