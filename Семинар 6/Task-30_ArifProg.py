#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

first_Number = int(input("Введите начальный элемент: "))
step_of_Progress = int(input("Введите шаг прогрессии: ")) 
amount_of_Numbers = int(input("Введите количество чисел: "))

''' Решение через формулу
# 2 5 8 11 13 16
for i in range(amount_of_Numbers):
        #2
        #print(i)
        print(first_Number + ((i+1)-1)*step_of_Progress)
'''
# Решение через range
r = range(first_Number, first_Number + amount_of_Numbers * step_of_Progress, step_of_Progress)
#           start           stop            step
for i in r:
    print(i)