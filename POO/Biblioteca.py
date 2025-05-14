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

#-----------------------------------------------------------------------
class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O {self.nome} latiu a noite inteira")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def pular(self):
        print(f"O {self.nome} pulou nos campos")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def leite(self):
        print(f"O {self.nome} deu leite")
    def capim(self):
        print(f"O {self.nome} foi comer capim")

#------------------------------------------------------------------------------------------

class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimevalor(self):
        print(f"O Ingresso custa R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)
    def imprimevalor(self):
        print(f"O Ingresso Vip custa R${self.valor:.2f}")

#------------------------------------------------------------------------------------------------
class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculoarea(self,base,altura):
        self.area = base * altura
        print(f"A area do retangulo é {self.area}")
    def calculoperimetro(self,base,altura):
        self.perimetro = (base+altura) * 2
        print(f"p perimetro do retangulo é {self.perimetro}")

class Triangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.altura = altura
        self.base = base
    def calculoarea(self):
        self.area = (self.base * self.altura)/2
        print(f"A area do triangulo é {self.area}")
    def calculoperimetro(self):
        self.perimetro = self.base*3
        print(f"P perimetro do triangulo é {self.perimetro}")
