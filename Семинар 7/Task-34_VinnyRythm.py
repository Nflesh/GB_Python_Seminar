text = list(input("Введите стих: ").split(" "))
count = []
vowels = ["а", "о", "У", "е", "ы", "э", "я", "и", "ю"]
def ritm(tekst):
    m=0
    for x in text:
        count.append(0)
        k=list(filter(lambda i: i in vowels, x))
        count[m]=len(k)
        m+=1
    for i in range(len(count)-1):
        if count[i]!=count[i+1]:
            print("Пам парам")
            return
    print("Парам пам-пам")
    return
ritm(text)
