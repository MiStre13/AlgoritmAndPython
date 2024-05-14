list = [1,1,1,1,1,6]
newDigit = 0
sumWhile = 0
circleWhile = 0
summa = 0

for i in list: 
    newDigit+=i
print(f"Вывод суммы через цикл for= {newDigit}")

while circleWhile < len(list):
    sumWhile += list[circleWhile]
    circleWhile += 1
print(f"Вывод суммы через цикл while= {sumWhile}")


def sumList(digit):
    global summa
    if digit == len(list):
        return
    summa += list[digit]
    sumList(digit+1)
sumList(0)
print(f"Вывод через рекурсивную функцию = {summa}")