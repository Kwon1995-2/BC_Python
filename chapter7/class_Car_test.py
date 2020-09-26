from class_Car import Car # import class_Car.Car -> error

mycar = Car('Black', 60)
print('색상:', mycar.color, '속도:',mycar.speed)
mycar.color = "Red"
print("색상:",mycar.color)
mycar.speedUp(10)
print("속도:",mycar.speed)
mycar.speedDown(20)
print("속도:",mycar.speed)