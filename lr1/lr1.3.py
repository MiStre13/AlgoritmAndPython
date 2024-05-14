word = str(input("Введите строку: "))
newString = ''

for i in word:
    newString=newString+i+'*'
print(newString[:-1])


wordNew = "*".join(word)
print(wordNew)