class Universite():

    def __init__(self):
        self.__vize = 0
        self.__final = 0

    def getVize(self):
        return self.__vize

    def setVize(self, parametre):

        if (parametre < 0 or parametre > 100):
            while True:
                print("Hatalı not aralığı girdiniz !")
                vizeNot = int(input("Vize Notunuz "))
                if vizeNot < 0 or vizeNot > 100:
                    continue
                else:
                    self.__vize = vizeNot
                    break
        else:
            self.__vize = parametre

    vize = property(getVize, setVize)

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, parametre):
        if (parametre < 0 or parametre > 100):
            while True:
                print("Hatalı not aralığı girdiniz !")
                finalNot = int(input("Final Notunuz "))
                if finalNot < 0 or finalNot > 100:
                    continue
                else:
                    self.__final = finalNot
                    break
        else:
            self.__final = parametre

    def ortlama(self):
        print("Dersin Ortalaması  :  ", ((self.__vize * 0.4) + (self.__final * 0.6)))
