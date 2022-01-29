#!../venv/bin/python3 
import math
import matplotlib.pyplot as plt
#ToDO
# V Реализовать класс точка
# V Реализовать класс треугольника
# V Реализовать проверку что точки не лежат на одной прямой
# Методы:
# V-Расстояние между двумя точками
# V-Площадь
# V-Периметр
# V-Точка пересечения медиан



class Point(object):
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.set_coord(x, y)

    def get_coord(self):
        return [self.__x, self.__y]

    def set_coord(self, x, y):
        if not isinstance(x, (float, int))  or not isinstance(y, (float, int)) :
            raise TypeError("Несоответствующий тип данных для координаты точки, тип данных должен быть целым или вещественным")
        self.__x = x
        self.__y = y


class Triangle(Point):

    def __init__(self, point_1, point_2, point_3):
        if not (isinstance(point_1, Point)) or not (isinstance(point_2, Point)) or not (isinstance(point_3, Point)):
            raise TypeError("Несоответствующий тип данных для точек треугольника")
        self.__points = [None] * 3
        self.__points[0] = point_1
        self.__points[1] = point_2
        self.__points[2] = point_3
        if not self.__is_triangle():
            raise ValueError("Точки треугольника лежат на одной прямой")
    def __is_triangle(self):
        dx_10 = (self.__points[1].get_coord()[0] - self.__points[0].get_coord()[0])
        dx_20 = (self.__points[2].get_coord()[0] - self.__points[0].get_coord()[0])
        dy_10 = (self.__points[1].get_coord()[1] - self.__points[0].get_coord()[1])
        dy_20 = (self.__points[2].get_coord()[1] - self.__points[0].get_coord()[1])
        if dx_10 == 0 and self.__points[2].get_coord()[0] != self.__points[0].get_coord()[0]:
            return True
        elif dy_10 == 0 and self.__points[2].get_coord()[1] != self.__points[0].get_coord()[1]:
            return True
        elif dy_10 != 0 and dx_10 != 0 and not math.isclose(dx_20/dx_10, dy_20/dy_10):
            return True
        else:
            return False

    @staticmethod
    def __distance(point_1, point_2):
        dx = (point_2.get_coord()[0] - point_1.get_coord()[0])
        dy = (point_2.get_coord()[1] - point_1.get_coord()[1])
        dist = math.sqrt(dx**2+dy**2)
        return dist

    def get_perimeter(self):
        length = list()
        length.append(self.__distance(self.__points[0], self.__points[1]))
        length.append(self.__distance(self.__points[1], self.__points[2]))
        length.append(self.__distance(self.__points[2], self.__points[0]))
        return sum(length)

    def get_area(self):
        length = list()
        length.append(self.__distance(self.__points[0], self.__points[1]))
        length.append(self.__distance(self.__points[1], self.__points[2]))
        length.append(self.__distance(self.__points[2], self.__points[0]))
        p = self.get_perimeter()/2
        area = math.sqrt(p*(p-length[0])*(p-length[1])*(p-length[2]))
        return area

    def get_median(self):
        x = list()
        y = list()
        for point in self.__points:
            x.append(point.get_coord()[0])
            y.append(point.get_coord()[1])
        median_x = sum(x) / len(x)
        median_y = sum(y) / len(y)
        median = Point(median_x, median_y)
        return median

    def print_points(self):
        for point in self.__points:
            print(point.get_coord())

    def plot_triangle(self):
        x = list()
        y = list()
        for point in self.__points:
            x.append(point.get_coord()[0])
            y.append(point.get_coord()[1])
        x.append(x[0])
        y.append(y[0])
        plt.plot(x, y)

        median = self.get_median()
        for point in self.__points:
            opposite_x = (median.get_coord()[0] * 3 - point.get_coord()[0]) / 2
            opposite_y = (median.get_coord()[1] * 3 - point.get_coord()[1]) / 2
            plt.plot([point.get_coord()[0], opposite_x], [point.get_coord()[1], opposite_y])

        plt.grid(visible="True")
        plt.show()


p1 = Point(0, 0)
p2 = Point(3, 5)
p3 = Point(7, 3)

t1 = Triangle(p1, p2, p3)
print(t1.get_perimeter())
print(t1.get_area())
print(t1.get_median().get_coord())
t1.print_points()
t1.plot_triangle()
