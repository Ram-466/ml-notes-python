def count_evens(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    return even_count
    
numbers = [3, 10, 5, 8, 2, 7]
print(count_evens(numbers))
