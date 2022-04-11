from Base import Base


class Product(Base):

    def __init__(self):
        self.price = 0
        self.stock = 0

    def Save(self):
        print("Kaydettim")

    def Delete(self):
        print("Sildim")

    def Update(self):
        print("Güncelledim")

    def List(self):
        print("Listeledim")