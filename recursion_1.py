def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

def factorial_recursive(n):
    fac = 1
    if n==1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)



number = int(input("Enter the number:\n"))
print(factorial_recursive(number))