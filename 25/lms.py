class User:
    __next_id = 0
    __id_dict = dict() # Словарь связывающий id и имя

    def __init__(self, name):
        self.__id = User.__next_id
        User.__next_id += 1
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь строковый тип")
        self.__name = name
        User.__id_dict[self.__id] = self.__name

    def __del__(self):
        del User.__id_dict[self.__id]

    def __str__(self):
        return self.__name + " " + str(self.__id)

    @property
    def id(self):
        return self.__id

    @staticmethod
    def get_name(id):
        if not isinstance(id, int):
            raise TypeError("id должен иметь целый тип")
        if id < 0:
            raise ValueError("id пользователя должен быть неотрицательным")
        if id not in User.__id_dict:
            raise ValueError("Нет пользователя с таким id")
        return User.__id_dict[id]


class Course:

    def __init__(self, course_name):
        if not isinstance(course_name, str):
            raise TypeError("Имя должно иметь строковый тип")
        self.__course_name = course_name
        self.__course_users = dict()

    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("В курс можно добавлять только пользователей")
        if user.id not in self.__course_users:
            self.__course_users[user.id] = None
        else:
            raise ValueError("Данный пользователь уже записан")

    def delete_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Из курса можно удалять только пользователей")
        if user.id in self.__course_users:
            self.__course_users.pop(user.id)
        else:
            raise ValueError("Данного пользователя нет на этом курсе")

    def set_mark(self, user, mark):
        if not isinstance(user, User):
            raise TypeError("Выставлять оценки можно только пользователям")
        if not (0 <= mark <= 100):
            raise ValueError('Значение оценки за курс вне диапазона 0..100')
        if user.id in self.__course_users:
            self.__course_users[user.id] = mark
        else:
            raise ValueError('Данный пользователь не записан на курс')

    def __str__(self):
        result_str = ""
        result_str +="Название курса: "+ self.__course_name+'\n'
        for key in self.__course_users:
            name = User.get_name(key)
            mark = self.__course_users[key]
            if not mark:
                mark = "Итоговая оценка не выставлена"
            result_str += name + " " + str(mark) + "\n"
        return result_str


u1 = User('Эвелина')
u2 = User('Олег')
u3 = User('Софья')
u4 = User('Максим')
u5 = User('Оливия')
u6 = User('Александра')
u7 = User('Арсений')
u8 = User('Алексей')
u9 = User('Андрей')
u10 = User('Елисей')
u11 = User('Елизавета')
u12 = User('Игорь')
u13 = User('Ева')




C1 = Course("Python разработчик")
C1.add_user(u7)
C1.add_user(u8)
C1.add_user(u9)
C1.add_user(u5)
print(C1)

C1.set_mark(u7, 50)
C1.set_mark(u8, 60)
C1.set_mark(u9, 70)
C1.set_mark(u5, 80)
print(C1)


C1.delete_user(u5)
print(C1)
