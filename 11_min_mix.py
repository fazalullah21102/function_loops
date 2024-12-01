def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

nums = [3, 7, 2, 8, 4, 10]
min_num, max_num = find_min_max(nums)
print(f"The minimum number is: {min_num}")
print(f"The maximum number is: {max_num}")
