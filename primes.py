def isPrime(n):
    # if n is equal to 2 return true (range of 2,2 is empty)
    # if n is divisible by the numbers in the range 2 to n(excluded)retur false
    # else retrun true
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def nthPrime(nth):
    return [i for i in range(2,nth*10) if isPrime(i)][nth+1]
    

n = int(input("enter number: "))

# print(f"{n} is prime: {is_prime(n)}")
print(f"Prime nº{n}: {nthPrime(n)}")
