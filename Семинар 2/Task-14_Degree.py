#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите число: "))
remainder = 1
while remainder < number:
    if(remainder < number):
        if (remainder * 2 > number):
            break
        else:
            remainder = remainder * 2
            print(remainder)
