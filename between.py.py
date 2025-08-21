numbers = list(range(1, 16))

numbers = [num for num in numbers if num % 3 != 0]

numbers.extend([num ** 2 for num in numbers])

numbers.reverse()

print(numbers)