# Задание 1.
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный
# метод running (запуск).
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("Red light. Stop!")
                sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Yellow light. Get ready!")
                sleep(2)
                self.__color = "green"
            else:
                print("Green light. Go!")
                sleep(5)
                self.__color = "red"


traffic_light = TrafficLight()
traffic_light.running()
