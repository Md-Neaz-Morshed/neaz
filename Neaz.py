def sum_of_even_numbers(start, middle, end):
    
    if start < middle < end:
        total_sum = 0
        for num in range(start, middle + 1):  
            if num % 2 == 0:  
                total_sum += num
        return total_sum
    else:
        return "Invalid input: start < middle < end must hold."


start = 3
middle = 10
end = 15

result = sum_of_even_numbers(start, middle, end)
print("Sum of even numbers between start and middle:", result)
