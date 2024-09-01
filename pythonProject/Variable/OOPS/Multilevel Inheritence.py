class car:
    def __init__(self, wheel, brake):
        self.wheel = wheel
        self.brake = brake
    def start(self):
        print("car stated")
    def stop(self):
        print("car stopped")

class toyota(car):
    def __init__(self, enginetype, wheel, brake):  #toyota constructor
        self.enginetype = enginetype
        super().__init__(wheel, brake)
class fortuner(toyota):
    def __init__(self, color, enginetype, wheel, brake):
        self.color = color
        super().__init__(enginetype, wheel, brake)

car1 = fortuner("white", "diesel", "four", "Hydraulic")
car1.start()
car1.stop()
print(car1.color)
print(car1.enginetype)
print(car1.wheel)
print(car1.brake)