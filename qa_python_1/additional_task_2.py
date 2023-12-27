def digit_root(num):
    def sum_of_digits_of_a_number(num):
        total_sum = 0
        for number in str(num):
            total_sum += int(number)
        return total_sum
    
    sum_of_digits = sum_of_digits_of_a_number(num)
    
    while sum_of_digits > 9:
        sum_of_digits = sum_of_digits_of_a_number(sum_of_digits)
    
    return sum_of_digits

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))