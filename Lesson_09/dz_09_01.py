class Car:
    def __init__(self, brand, color, engine_volume):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume

    def go_forvard(self):
        print("Їду вперед")

    def go_back(self):
        print("Їду назад")

class Track(Car):
    def go_left(self):
        print("Їду на ліво")

    def go_right(self):
        print("Їду на право")

ford = Track('ford', 'black', 5.7)
ford.go_left()
ford.go_right()
ford.go_forvard()
ford.go_back()
print(ford.brand)
print(ford.color)
print(ford.engine_volume)