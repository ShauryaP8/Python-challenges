def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(3)
print(result)

#Example of a recursive function