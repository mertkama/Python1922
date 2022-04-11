#### ABSTRACTION (Abstract,Interface) #####
'''
Abstract class(soyut sınıf): Abstract sınıfların kullanım amacı tanımlanan bir class'ın
sadece base class özelliği taşıması sağlamaktır.
Python dilinde diğer dillerden farklı olarak abstract yapısı
 hazır olarak tanımlıdır ve import edilmesi gereklidir.
Abstract class'lar da tanımlanan field(özellik,attribute)'lara değer
 atanmaz ve metotların gövdeleri doldurulmaz. Yani amac sadece
  tanımlama(miras alındığında türeyen sınıfa aktarılması istenen özellikler).

Abstract methodlar sadece Abstract(ABC) class'larda bulunurlar ama
 class Abstract diye bütün methodlar @abstractmethod olmak zorunda değil.
'''

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def Drink(self):
        pass

    @abstractmethod
    def  Walk(self):
        pass

    @abstractmethod
    def Sleep(self):
        pass

class Bird(Animal):
    pass


b = Bird()