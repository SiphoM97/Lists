sports = ["soccer", "rugby", "skating", "swimming"]

print(sports[0])

# list comprehension

nums = [1, 4, 78, 30, 15]
doubled = []

for num in nums:
    doubled.append(num * 2)

    print(doubled)

#List comprehensions to solve these types of problems in one line.

nums = [1, 4, 78, 30, 15]
doubled = [num * 2 for num in nums]
print(doubled)