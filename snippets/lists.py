numbers = [10, 20, 30, 40]

print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(50)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

total = 0
for num in numbers:
    total += num

print("Sum:", total)
