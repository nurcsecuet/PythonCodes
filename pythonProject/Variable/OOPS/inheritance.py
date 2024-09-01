class car:
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")

class toyota(car):
    def manufactured(self):
        print("Manufactured in Japan")

class ford(car):
    def manufactured(self):
        print("Manufactured in USA")

car1 = car()
car1.start()
car1.stop()
#Creating objects of toyeta class

# toyota1 = toyota()
# toyota1.manufactured()
# toyota1.start()

ford1 = ford()
ford1.stop()