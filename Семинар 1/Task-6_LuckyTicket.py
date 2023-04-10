numberOfTicket = input("Введите номер билета:")

left = 0
right = 0

for i in range(3):
    left += int(numberOfTicket[i])
    
for i in range(3,6):
    right += int(numberOfTicket[i])

if left == right:
    print("Поздравляю, Ваш билет счастливый!")
else:   
    print("Жаль, но Ваш билет не счастливый")