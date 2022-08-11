import math

print("Ваш персональный кукулятор")
print("\n Для справки введите help \n Для вычислений нажмите любую клавишу \n")

while True:
    start = input()
    if start == "help":
        print("\nВас приветствует PcCalculator v. 1.3 \n\n Вводите 2 любых числа от 350000000 до -350000000 (целое/десятичное) \n Затем знак вычисления")
        print(" Десятичные числа вводятся с помощью точки \n\nДоступные команды: \n+  сложение \n-  вычитание \n*  умножение \n/  деление \n%  деление с остатком (по модулю)")
    #elif start == "start": print("Let's do it")
    #else: print("Неверный аргумент")

    while True:
        try:
            num1 = input("\n1 число: ")
            if num1 == "help":
                print("\n Вводите 2 любых числа от 350000000 до -350000000 (целое/десятичное) \n Затем знак вычисления \n Десятичные числа вводятся с помощью точки")
            else:
                num1 = float(num1)
                break
        except ValueError:
            print("Неверный аргумент! Введи число \nВведите help для вывода списка доступных команд")

    while True:
        if num1 <= 350000000 or num1 >= -350000000:
            try:
                num2 = input("\n2 число: ")
                if num2 == "help":
                    print("\n Вводите 2 любых числа от 350000000 до -350000000 (целое/десятичное) \n Затем знак вычисления \n Десятичные числа вводятся с помощью точки")
                else:
                    num2 = float(num2)
                    break
            except ValueError:
                print("Неверный аргумент! Введи число \nВведите help для вывода списка доступных команд")
        else: print("Введи число поменьше")

    while True:
        if num2 <= 350000000 or num2 >= -350000000:
            sign = input("\nЗнак действия: ")
        else: print("Введи число поменьше")


        if sign == "+":
            num1 += num2
            if num1 % 1 == 0:
                num3 = int(num1)
                print("Сумма ваших чисел: " + str(num3))
            #printf("%8.2f", num1); // выводим цифры после запятой(в данном случае 2 цифры)
            # f - буква f перед строкой указывает на то, что это f-строка, что является удобным способом форматирования текстовой строки.
            else:
                print(f"Сумма ваших чисел: " + str(num1))
            break

        elif sign == "-":
            num1 -= num2
            if num1 % 1 == 0:  #убираем нули после запятой альтернатива(num1 == int(num1))
                num3 = int(num1)
                print("Разность ваших чисел: " + str(num3))
            else:
                print("Разность ваших чисел: " + str(num1))
            break

        elif sign == "/":
            num1 /= num2
            if num1 == int(num1):
                num3 = int(num1)
                print("Частное ваших чисел: " + str(num3))
            else:
                print("Частное ваших чисел: " + str(num1))
            break

        elif sign == "*":
            num1 *= num2
            if num1 == int(num1):
                num3 = int(num1)
                print("Произведение ваших чисел: " + str(num3))
            else:
                print("Произведение ваших чисел: " + str(num1))
            break

        elif sign == "%":
            num1 %= num2
            if num1 == int(num1):
                num3 = int(num1)
                print("Остаток от деления ваших чисел: " + str(num3))
            else:
                print("Остаток от деления ваших чисел: " + str(num1))
            break

        elif sign == "help":
            print("\nДоступные команды: \n+  сложение \n-  вычитание \n*  умножение \n/  деление \n%  деление с остатком (по модулю)")

        else:
            print("Неверная команда. Введите help для вывода списка доступных команд")
    break
