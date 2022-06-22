sum = 0
num = 0

while num < 1000:
    num += 1
    if num % 3 != 0: continue

    sum += num

print(sum)