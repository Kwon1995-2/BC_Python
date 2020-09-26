# class 선언 방법
class Car:
    def __init__(self, color, speed): # : block을 가지고 있다. #메소드에서 self default -> 호출 시, 사용x
        self.color = color
        self.speed = speed

    def speedUp(self, v):
        self.speed = self.speed + v
        return self.speed
    def speedDown(self, v):
        self.speed = self.speed - v
        return self.speed


