def count_pairs(lst, target):
    count = 0
    num_dict = {}

    for num in lst:
        complement = target - num
        if complement in num_dict:
            count += num_dict[complement]
        num_dict[num] = num_dict.get(num, 0) + 1

    return count

# Example usage:
lst = [2, 3, 5, 7, 8]
target = 10

result = count_pairs(lst, target)
print(result)
