# This function computes the factors of the argument passed
def factor(n):
    print(f"The factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


num = int(input("Please enter the number to find factors: "))
print("Factors of the number are:", factor(num))
