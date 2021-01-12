class Vehicle:

    def __init__(self, marca, nome, ano, cor, tipo):

        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.tipo = tipo
        #tipo = carroceria


    def to_file_string(self):

        return (self.marca + "|" +
		self.nome + "|" +
		str(self.ano) + "|" +
		self.cor + "|" +
		self.tipo + "|" + "\n")


    def show_status(self):

        print("Marca: " + self.marca + ",  Nome: " + self.nome +
              ", Ano: " + str(self.ano) + ", Cor: " + self.cor +
              ", Tipo: " + self.tipo
              + "\n")