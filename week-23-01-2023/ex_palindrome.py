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

def d_palindrome (n:int) -> bool:
    n=n//100
    n=inverse(n)
    n=n//100
    n=inverse(n)
    if is_palindrome(n):
        return True
    else:
        return False


n = int(input("Please type in a number: "))

s=d_palindrome(n)

if s:
    print("The number "+ str(n) + " is a d_palindrome")
else:
    print("The number "+ str(n) + " is not a d_palindrome ")