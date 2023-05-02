
def doingPow(num, pow):
    if pow == 1:   
        return num
    elif pow == 0:
        return 1 
    elif pow < 0:
        print("Введите положительную степень: ")
        return -1
        
    return num * doingPow(num,pow-1)


number = int(input("Введите число: "))
input_Pow = int(input("Введите степень: "))


print(f"Итог {doingPow( number, input_Pow)}")



