def sum (first, second):
    if first == 0:
        return second
    elif second == 0:
        return first
    elif first < 0 or second < 0:
        print("Введите положительное значение")
        return -1

    first = first + 1
    second = second - 1
    print( f'{first} + {second}')
    return sum(first,second)
    
    
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print(f'Итог: {sum(first_number, second_number)}')

