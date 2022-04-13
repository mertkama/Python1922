from abc import ABC, abstractmethod


class Base(ABC):

    def __init__(self):
        self.id = ""
        self.name = ""
        self.addDate = ""
        self.updateDate = ""
        self.deletedDate = ""

    @abstractmethod
    def Save(self):
        pass

    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def Update(self):
        pass

    @abstractmethod
    def List(self):
        pass
