import random
import textwrap
import time
import hashlib
import math
import libs

print(f"Игра 'Угадай число'")
num = random.randrange(0, 100, 2)
print(f"Введите число, которое, по вашему мнению, загадал компьютер")
#print(num) #проверка

z = 0
def out():
    global z
    while True:
        while True:
            try:
                numPlayer = input()
                if numPlayer == "Стоп":
                    return
                else:
                    numPlayer = float(numPlayer)
                    break
            except ValueError:
                print("Введите число")
        z += 1
        if numPlayer > num:
            print("Моё число меньше вашего")
        elif numPlayer < num:
            print("Моё число больше вашего")
        else:
            print("Поздравляю, вы угадали за " + str(z) + " попыток!")
            break
out()