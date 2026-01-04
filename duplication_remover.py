def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

nums = [1,5,2,3,4,4,6]
unique = remove_duplicates(nums)
print(unique)
