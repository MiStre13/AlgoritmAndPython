def count_digits(num):
    num_str = str(num)  
    unique_digits = set(num_str)  
    digits_count = {digit: num_str.count(digit) for digit in unique_digits}  

    for digit, count in digits_count.items():
        print(f"Цифра: {digit}, Количество: {count}")

# Пример использования
number = int(input("Введите число: "))
print(f"Число: {number}")
count_digits(number)
