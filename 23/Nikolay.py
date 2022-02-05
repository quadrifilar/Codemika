class Nikola(object):

    @staticmethod
    def check_age(age):
        if isinstance(age, int):
            if age <= 0:
                raise ValueError("Возраст должен быть положительным")
        else:
            raise TypeError("Возраст должен быть целым числом")
        return age

    def __init__(self, age):
        self._name = "Николай"
        self._age = self.check_age(age)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Тип имени должен быть строка")
        if name != "Николай":
            print("Я не " + name + ", а Николай")
            self._name = "Николай"

    def __str__(self):
        return self._name+" " + str(self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = self.check_age(age)




N = Nikola(-5)
N.name = "Df"
print(N.name)
print(N)

