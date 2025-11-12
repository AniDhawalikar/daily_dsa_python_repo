# input : n = 123
# output : 6

def digit_sum(n):
    sum = 0
    while n > 0:
        last_digit = n%10
        sum +=last_digit
        n = n//10
    return sum

num = 123123456789009876543212345678
print(digit_sum(num))
