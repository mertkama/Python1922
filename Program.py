class Program:

    def __init__(self):
        self._sayi = 0

    @property  # Getter özelliğin değerini döndürür
    def sayi(self):
        return self._sayi

    @sayi.setter  # Setter özelliğe değer atar
    def sayi(self, value):

        if value % 2 == 0:
            self._sayi = value
        else:
            print("Sadece Çift Sayı Girin")

    @sayi.deleter  # Deleter özelliği siler
    def sayi(self):
        print("Değer siliniyor")
        del self._sayi


num1 = Program()
num1.sayi = 6
del num1.sayi
print(num1.sayi)
