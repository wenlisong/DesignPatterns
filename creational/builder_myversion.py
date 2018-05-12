# My builder example

class Cook(object):
    def __init__(self):
        self.cook_staple()
        self.make_beverage()

    def cook_staple(self):
        raise NotImplementedError

    def make_beverage(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Staple: {0.staple} | Beverage: {0.beverage}'.format(self)


class ChineseCook(Cook):
    def cook_staple(self):
        self.staple = 'Rice'

    def make_beverage(self):
        self.beverage = 'Soup'


class USCook(Cook):
    def cook_staple(self):
        self.staple = 'Steak'

    def make_beverage(self):
        self.beverage = 'Cola'


class Director(object):
    def arrange_cook(self, cook):
        self.cook = cook()
        self.cook.cook_staple()
        self.cook.make_beverage()
        return self.cook


def main():
    director = Director()
    cook1 = director.arrange_cook(ChineseCook)
    cook2 = director.arrange_cook(USCook)
    print(cook1)
    print(cook2)


if __name__ == '__main__':
    main()
