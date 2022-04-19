class Student(object):

    def __init__(self):
        self._no = ""

    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, val):
        self._no =  val


s = Student()
s.no = 35
print(s.no)