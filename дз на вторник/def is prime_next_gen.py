def is_prime (number):
    if number > 1:
        for  num in range(2, number):
            if number % num == 0:
                return False
            else:
                 return True

number = int(input())
is_prime(number)
print(is_prime)






