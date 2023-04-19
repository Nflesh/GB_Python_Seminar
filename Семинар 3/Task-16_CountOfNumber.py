# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

endOfArray = int(input("Введите последний элемент массива:"))
listOfNumber = list()

for i in range(endOfArray):
    listOfNumber.append(i+1)

listOfNumber.append(4)
listOfNumber.append(4)
print(listOfNumber)

compareNumber = int(input("Введите искомое число:"))

counter = 0

print(len(listOfNumber))
for i in range(len(listOfNumber)):
    if compareNumber == listOfNumber[i]:
        counter+=1
    

print(f"Кол-во совпадений = {counter}")


