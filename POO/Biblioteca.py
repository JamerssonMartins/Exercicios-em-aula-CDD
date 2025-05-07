class Pessoa():
    def __init__(self, user):
        self.nome = user
        self.estado = "parado"

    def dormir(self):
        if self.estado == "dormindo":
            print(f"O {self.nome} está {self.estado}")
        elif self.estado == "falando" or "comendo":
            print(f"O {self.nome} não pode {self.estado} pois está dormindo")
        elif self.estado == "dormindo":
            print(f"O {self.nome} já está dormindo")
    def falar(self):
        if self.estado == "falando":
            print()
    def comer(self):
        if self.estado == "comendo":
            print()
    def parar(self):
        print(f"O {self.nome} parou de {self.estado}")



