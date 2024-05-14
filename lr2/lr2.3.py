def count_equal_pairs(nums):
    num_count = {}
    pair_count = 0

    for num in nums:
        if num in num_count:
            pair_count += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1
    return pair_count

nums = [1, -1, 2, 3, -5, 1, 2, -8, -9, 2]

print(count_equal_pairs(nums))

