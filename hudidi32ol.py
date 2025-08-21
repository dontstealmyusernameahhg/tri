class BMW:
    def car_info(self):
        print("This is a BMW car.")

    def speed(self):
        print("BMW speed: 240 km/h")


class Ferrari:
    def car_info(self):
        print("This is a Ferrari car.")

    def speed(self):
        print("Ferrari speed: 340 km/h")


# Polymorphism: same method name, different behavior
def show_car_details(car):
    car.car_info()
    car.speed()


# Create objects
bmw = BMW()
ferrari = Ferrari()


# Call same methods on different objects
show_car_details(bmw)
show_car_details(ferrari)