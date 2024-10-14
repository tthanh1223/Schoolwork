"""Amstrong number is a number that is = the sum of its digit each raised to the power of the number of digits in the number.
Check"""
def count_digit(number):
    return len(str(number))
def check_amstrong_number(number):
    sum_digit = 0
    for i in str(number):
        sum_digit += int(i)**(len(str(number)))
    return sum_digit == number

a = int(input("Enter a number: "))
print(check_amstrong_number(a))
