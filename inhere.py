class cars():
    def __init__(self, marks):
        self.marks = marks


car1 = cars(5)

car2 = car1
print(car1)
print(car2)

car1.marks = 6
print(car2.marks)

a = 5
b = a
print(a, b)

a = 6
print(a, b)