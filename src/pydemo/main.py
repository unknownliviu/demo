from pydemo.helper import test_function
from pydemo.waterbottle.bottle import drink


class Cat(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def meow(self):

        return "meow"


if __name__ == "__main__":
    c = Cat("Feli")
    print(c)
    test_function()
    drink()
