import re

newPalindrom = input("Введите строку: ")
deleteSigns = re.sub(r'[.,"\'-?:!; ]', '', newPalindrom)
deleteSigns.replace(' ', '')

deleteSigns = deleteSigns.lower()

reversedString = deleteSigns[::-1]

# print(deleteSigns)
# print(reversedString)


if deleteSigns == reversedString:
    print("Yes")
else:
    print("No")