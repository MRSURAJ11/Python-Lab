class Grandfather:

    def __init__(self):
        self._house = "Big House"      # Protected variable
        self.__money = 50000            # Private variable

    def _show_house(self):              # Protected function
        print("House:", self._house)

    def __show_money(self):             # Private function
        print("Money:", self.__money)


class Father(Grandfather):

    def show_father(self):
        print("Father can access protected variable:", self._house)
        self._show_house()


class Son(Father):

    def show_son(self):
        print("Son can access protected variable:", self._house)
        self._show_house()


s = Son()

s.show_father()
s.show_son()