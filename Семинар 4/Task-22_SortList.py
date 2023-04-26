
lenght_first = int(input("Введите длину первого массива: "))
lenght_second = int(input("Введите длину второго массива: "))
    
print("Заполнение 1-ого массива")
lst1 = []
for i in range(lenght_first):
    lst1.append(int(input(f"Введите {i+1} элемент ")))
        
print("Заполнение 2-ого массива")
lst2 = []
for i in range(lenght_second):
    lst2.append(int(input(f"Введите {i+1} элемент ")))
       
set1 = set(lst1)
set2 = set(lst2)
    
duplicates = sorted(set1 & set2)
   
print(lst1)
print(lst2)
print(duplicates)