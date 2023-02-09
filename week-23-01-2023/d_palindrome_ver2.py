def inverse(n: int) -> int:
    # inverse(123) -> 321

    inv = 0
    while (n != 0):
        inv = inv * 10 + n % 10
        n = n // 10
    return inv


def is_palindrome(n: int) -> bool:
    # is_palindrome(12321) -> True
    # is_palindrome(12341) -> False
    
    if n == inverse(n):
        return True
    else:
        return False



def extract_even_digits(n: int) -> int:
    # extract_even_digits(123456) -> 246
    
    x = 0
    p = 1
    while(n >99):
        d = n % 10
        x = d * p + x
        p = p * 10
        n = n // 10
    return x

n = int(input("Please type in a number: "))
n=n//100
r = extract_even_digits(n)

if is_palindrome(r):
    print("The number "+ str(n) + " is a d_palindrome")
else:
    print("The number "+ str(n) + " is not a d_palindrome ")