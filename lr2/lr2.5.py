def check_previous_numbers(sequence):
    numbers = sequence.split()
    seen_numbers = set()  

    for number in numbers:
        if number in seen_numbers:
            print('YES')
        else:
            seen_numbers.add(number)
            print('NO')


input_sequence = "1 2 3 1 4 5 2"
check_previous_numbers(input_sequence)
