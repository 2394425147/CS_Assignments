numbers1 = [11, 12, 13, 14, 15, 18, 20, 16, 17, 19]
numbers2 = []
numbers3 = []

# 1. Copy numbers from numbers1 to numbers2 and print the results
numbers2.extend(numbers1)
print(numbers2)

# 2. Copy numbers from numbers1 ranging from 3 to 8 to numbers3
# and print the results
numbers3.extend(numbers1[3:9])
print(numbers3)

# 3. Print the extreme values and the mean of numbers1
print(max(numbers1))
print(min(numbers1))
print(sum(numbers1) / len(numbers1))

# 4. Sort numbers1 and print the results
numbers1.sort()
print(numbers1)
