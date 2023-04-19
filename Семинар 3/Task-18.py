# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X



endOfArray = int(input("Введите последний элемент массива:"))
listOfNumber = list()

listOfNumber = [i for i in range(endOfArray) if i % 2 == 0]

print(listOfNumber)
print(listOfNumber[len(listOfNumber)-1])
compareNumber = int(input("Введите искомое число:"))

for i in range(len(listOfNumber)):
    if compareNumber > listOfNumber[len(listOfNumber)-1]:
        print(f"Ближайшее число {listOfNumber[len(listOfNumber)-1]}")
        break
    elif compareNumber < listOfNumber[0]:
        print(f"Ближайшее число {listOfNumber[0]}")
        break
    elif  listOfNumber[i] == compareNumber:
        print(f"{compareNumber} равняется {i+1}му элементу массива")
        break
    elif  listOfNumber[i+1]> compareNumber > listOfNumber[i]:
        print(f"{compareNumber} находится между {listOfNumber[i]} и {listOfNumber[i+1]}")
        break
