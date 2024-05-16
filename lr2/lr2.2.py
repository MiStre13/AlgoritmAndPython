import random
spisok_primer = random.sample(range(-10, 10), 10)
print(spisok_primer)

def f(spisok):

  i = 0
  j = len(spisok) - 1
  while i <= j:
    if spisok[i] >= 0:
      spisok[i], spisok[j] = spisok[j], spisok[i]
      j -= 1
    else:
      i += 1
  return spisok
spisok=f(spisok_primer)
print(f(spisok))