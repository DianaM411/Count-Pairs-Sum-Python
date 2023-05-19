def count_pairs(numbers, target):
    count = 0
    num_dict = {}

    for num in numbers:
        complement = target - num
        if complement in num_dict:
            count += num_dict[complement]
        num_dict[num] = num_dict.get(num, 0) + 1

    return count

# Example usage:
numbers = [2, 3, 5, 7, 8]
target = 10

result = count_pairs(numbers, target)
print(result)
