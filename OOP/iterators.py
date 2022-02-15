from random import randint


class RandomNum(object):
    def __init__(self, qnt, start, finish):
        self.qnt = qnt
        self.start = start
        self.finish = finish

    def __iter__(self):
        return self

    def __next__(self):
        if self.qnt > 0:
            self.qnt -= 1
            return randint(self.start, self.finish)
        else:
            raise StopIteration


s = RandomNum(5, 1, 100)
for i in s:
    print(i)
