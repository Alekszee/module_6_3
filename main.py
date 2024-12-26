import random


class Animal :
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed) :
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz) :
        __X = self._cords[0] + dx * self.speed
        __Y = self._cords[1] + dy * self.speed
        __Z = self._cords[2] + dz * self.speed
        if __Z < 0 :
            print("It's too deep, i can't dive :(")
        else :
            self._cords = [__X, __Y, __Z]

    def get_cords(self) :
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self) :
        if self._DEGREE_OF_DANGER < 5 :
            print("Sorry, i'm peaceful :)")
        else :
            print("Be careful, i'm attacking you 0_0")

    def speak(self) :
        print(self.sound)


class Bird(Animal) :
    beak = True

    def lay_eggs(self) :
        _eggs = random.randint(1, 4)
        print(f'Here are(is) {_eggs} eggs for you')


class AquaticAnimal(Animal) :
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz) :
        __Z = self._cords[2] - abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal) :
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal,  AquaticAnimal ) :
    sound = "Click-click-click"

    def __init__(self, speed) :
        super().__init__(speed)




db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

# print(Duckbill.mro())
# Вывод на консоль:
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you # Число может быть другим (1-4)
#
