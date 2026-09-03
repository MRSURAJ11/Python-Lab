class Father:
    def car(self):
        print("Father has a car")


class Mother:
    def house(self):
        print("Mother has a house")


class Son(Father, Mother):
    pass


s = Son()

s.car()
s.house()