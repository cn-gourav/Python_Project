a = int(input("Enter a number : "))


# factorialNumber 
def factorialNumber(a):
    fac = 1
    for i in range(1 ,a+1):
        fac = fac * i
    return fac

result = factorialNumber(a)
print("Factorial of",a,"is: ",result)
