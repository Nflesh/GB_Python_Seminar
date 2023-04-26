number_of_seed_bed = int(input("Введите число грядок: "))
lst = list()
for i in range(number_of_seed_bed):
    number_of_berry = int(input(f" Введите количество ягод на {i+1} клумбе: "))
    lst.append(number_of_berry)

lst_count = list()
for i in range(len(lst)-1):
    lst_count.append(lst[i-1] + lst[i] + lst[i+1])
lst_count.append(lst[-2] + lst[-1] + lst[0])
print(max(lst_count))