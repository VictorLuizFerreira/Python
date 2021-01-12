import os
from OldCodes.concessionaria.visao import obj
from OldCodes.concessionaria.arquivos import Files
from OldCodes.concessionaria.veiculo import Vehicle


class Main:

    def adicionar_veiculo(self):

        a = obj("Marca: ", "Nome: ", "Ano: ", "Cor: ", "Tipo: ")

        fl = Files()

        fl.writeToFile(a, "veiculos.txt")

    def deletar_veiculo(self):

        veiculos = self.carregar_veiculo()

        for veic in veiculos:
            veic.show_status()

        a = obj("Marca: ", "Nome: ", "Ano: ", "Cor: ", "Tipo: ")

        fl = Files()

        fl.deleteFile(a, "veiculos.txt")

    def carregar_veiculo(self):

        fl = Files()

        veic = fl.readFile("veiculos.txt")

        result = []

        for v in veic:
            params = v.split("|")

            vc = Vehicle(params[0], params[1], params[2],
                         params[3], params[4])

            result.append(vc)

        return result

    def mostrar_veiculo(self):

        veiculos = self.carregar_veiculo()

        for veics in veiculos:
            veics.show_status()

    def procurar_veiculo(self):

        marc = input("Digite a marca: \n")

        os.system("cls")

        fl = Files()

        veic = fl.readFile("veiculos.txt")

        result = []

        for i in veic:

            veic_list = i.split("|")

            if veic_list[0] == marc:
                vc = Vehicle(veic_list[0], veic_list[1], veic_list[2],
                             veic_list[3], veic_list[4])

                result.append(vc)

        for veics in result:
            veics.show_status()

    def main_menu(self):

        menu_option = {"1": self.adicionar_veiculo,
                       "2": self.deletar_veiculo,
                       "3": self.mostrar_veiculo,
                       "4": self.procurar_veiculo,
                       "0": exit}

        option = "entrada"

        while option != "0":

            try:

                option = input("1. Adicionar Veiculo \n" +
                               "2. Deletar Veiculo \n" +
                               "3. Mostrar Veiculo(s) \n" +
                               "4. Procurar Veiculo \n" +
                               "0. Sair \n")

                os.system("cls")

                menu_option[option]()



            except KeyError:

                os.system("cls")

                input("Erro. Enter para continuar\n")


mg = Main()
mg.main_menu()