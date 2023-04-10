heightOfChocolate = int(input("Введите высоту шоколадки:"))
widthOfChocolate = int(input("Введите ширину шоколадки:"))

numberOfCuttingSlice = int(input("Введите количество долек, которые вы хотите отрезать:"))

if (numberOfCuttingSlice % heightOfChocolate) ==  0: 
    print("Можно отрезать")
elif (numberOfCuttingSlice % widthOfChocolate) == 0:
    print("Можно отрезать")
else:
    print("Нельзя отрезать")
