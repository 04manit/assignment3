def factorial(x):
    ans=1
    for i in range(x,1,-1):
        ans = ans * i
    return ans

num = int(input("Enter a number : "))
print("Factorial of", num, "is", factorial(num))