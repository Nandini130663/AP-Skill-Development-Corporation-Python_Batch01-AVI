def is_palindrom(s):
    if(s == s[::-1]):
        return True
    return False

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f