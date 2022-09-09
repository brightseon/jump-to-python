from random import randint

numbers = []

while len(numbers) < 6:
    num = randint(1, 45)

    if num in numbers:
        continue

    numbers.append(num)

print(numbers)
