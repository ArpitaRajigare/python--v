def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")

if is_palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

if is_perfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
