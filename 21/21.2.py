from datetime import datetime, date, time, timedelta
#ToDo
# Иерархия классов:
# -V Интервал -> Временной интервал
# Поля:
#  -V Начало
#  -V Окончание
#  -V Длительность
# Методы:
# -V Изменение начала
# -V Изменение конца
# Проверки:
# -V Конец должен быть после начала


class Interval (object):
    @staticmethod
    def check_types(begin, end):
        if not isinstance(begin, type(end)):
            raise TypeError("Границы интервала имеют различный тип")

    @staticmethod
    def check_sequence(begin, end):
        if begin <= end:
            return True
        else:
            return False

    @staticmethod
    def difference(begin, end):
        return end - begin

    def __init__(self, begin, end):
        self.check_types(begin, end)
        if self.check_sequence(begin, end):
            self.__begin = begin
            self.__end = end
            self.__duration = self.difference(self.__begin,self.__end)
        else:
            raise ValueError("Значение конца интервала должно быть не раньше начала")

    def set_begin(self, begin):
        self.check_types(begin, self.__end)
        if self.check_sequence(begin, self.__end):
            self.__begin = begin
            self.__duration = self.difference(self.__begin,self.__end)
        else:
            raise ValueError("Значение конца интервала должно быть не раньше начала")

    def set_end(self, end):
        self.check_types(self.__begin, end)
        if self.check_sequence(self.__begin, end):
            self.__end = end
            self.__duration = self.difference(self.__begin,self.__end)
        else:
            raise ValueError("Значение конца интервала должно быть не раньше начала")

    def __str__(self):
        s = "begin= "+str(self.__begin)+'\n'
        s += "end= " + str(self.__end)+'\n'
        s += "duration= " + str(self.__duration)
        return s


class TimeInterval(Interval):
    @staticmethod
    def check_types(begin, end):
        if not isinstance(begin, type(end)):
            raise TypeError("Границы интервала имеют различный тип")
        correct_types = (datetime, date, time)
        if not isinstance(begin, correct_types) or not isinstance(end, correct_types):
            raise TypeError("Границы интервала имеют тип не соответсвующий временному диапазону")

    @staticmethod
    def difference(begin, end):
        if isinstance(begin, time) and isinstance(end, time):
            begin_delta = timedelta(hours=begin.hour, minutes=begin.minute, seconds=begin.second)
            end_delta = timedelta(hours=end.hour, minutes=end.minute, seconds=end.second)
            delta = end_delta-begin_delta
            return delta.total_seconds()
        else:
            return end - begin

    @staticmethod
    def check_sequence(begin, end):
        if begin <= end:
            return True
        else:
            return False


i_1 = Interval(10, 20)
print(i_1)
i_1.set_end(11)
i_1.set_begin(6)
print(i_1)


d_1 = date(2005, 7, 14)
t_1 = time(12, 30)
dt_1 = datetime.combine(d_1, t_1)

d_2 = date(2005, 7, 15)
t_2 = time(15, 26)
dt_2 = datetime.combine(d_2, t_2)

i_2 = TimeInterval(dt_1, dt_2)
print(i_2)
