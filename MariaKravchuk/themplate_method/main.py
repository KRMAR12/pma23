from abc import ABC, abstractmethod
class CheifCook(ABC):
    @abstractmethod
    def wash(self):
        pass

    @abstractmethod
    def chop(self):
        pass

    @abstractmethod
    def fry(self):
        pass

    def cook(self):
        self.wash()
        self.chop()
        self.fry()


class MakeSalad(CheifCook):
    def wash(self):
        print("Wash vegetables")

    def chop(self):
        print("Chop vegetables")

    def fry(self):
        print("Fry salad")


class CookMeat(CheifCook):
    def wash(self):
        print("Wash meat")

    def chop(self):
        print("Chop meat")

    def fry(self):
        print("Fry meat")


make_salad = MakeSalad()
make_salad.cook()
print(25 * "-")

cook_meat = CookMeat()
cook_meat.cook()
