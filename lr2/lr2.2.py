from random import randint

count_digit = int(input("Введите длину списка: "))
random_list = []
for i in range(count_digit):
    random_list.append(randint(-10,10))
print("Исходный список:", random_list)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def rearrange_list(lst):
    right = 0 
    left = 0 

    while right < len(lst):
        if lst[right] < 0:
            swap(lst, left, right)
            left+=1
        right += 1

    # for num in lst:
    #     if num < 0:
    #         negative_nums.append(num)
    #     else:
    #         positive_nums.append(num)
            
    # rearranged_list = negative_nums + positive_nums

    # return rearranged_list


rearranged = rearrange_list(random_list)
print("Преобразованный список:", rearranged)

