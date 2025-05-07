class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.estado = "parado"  # pode ser: parado, comendo, falando, dormindo

    def falar(self):
        if self.estado == "falando":
            print(f"{self.nome} já está falando.")
        elif self.estado in ["comendo", "dormindo"]:
            print(f"{self.nome} não pode falar enquanto está {self.estado}.")
        else:
            self.estado = "falando"
            print(f"{self.nome} começou a falar.")

    def comer(self):
        if self.estado == "falando":
            print(f"{self.nome} não pode comer enquanto está falando.")
        else:
            self.estado = "comendo"
            print(f"{self.nome} começou a comer.")

    def dormir(self):
        if self.estado == "falando":
            print(f"{self.nome} não pode dormir enquanto está falando.")
        else:
            self.estado = "dormindo"
            print(f"{self.nome} foi dormir.")

    def parar(self):
        print(f"{self.nome} parou de {self.estado}.")
        self.estado = "parado"
