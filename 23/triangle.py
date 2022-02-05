class TriangleChecker(object):
    @staticmethod
    def is_triangle(l1, l2, l3):
        if not (isinstance(l1, int) and isinstance(l2, int) and isinstance(l3, int)):
            print("Нужно вводить только числа!")
            return None
        if l1 <= 0 or l2 <= 0 or l3 <= 0:
            print("С отрицательными числами ничего не выйдет!")
            return None
        if l1+l2 <= l3 or l1+l3 <= l2 or l2+l3 <= l1:
            print("Жаль, но из этого треугольник не сделать.")
            return None
        else:
            print("Ура, можно построить треугольник!")
            return [l1, l2, l3]

    def __init__(self, l1, l2, l3):
        length_list = self.is_triangle(l1, l2, l3)
        if length_list:
            self.__l1, self.__l2, self.__l3 = length_list
        else:
            print("Значения длин некорректны")

    def __str__(self):
        return str(self.__l1) + ", " + str(self.__l2) + ", " + str(self.__l3)


t1 = TriangleChecker(10, 2, 10)
print(t1)
