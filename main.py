from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на наса напали!')
        pipls = 100
        for i in range(pipls):
            pipls -= self.power
            print(f'{self.name} сражаются {i + 1} дней, осталось количество воинов {pipls}'"\n")
            sleep(1)
            if pipls == 0:
                print(f"{self.name} одержал победу спустя {i + 1} дней!"'\n')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")