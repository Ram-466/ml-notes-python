def find_max(numbers):
    max_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
            
    return max_value
    
numbers = [4, 12, 7, 25, 3]
print(find_max(numbers))
