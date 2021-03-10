def genFibo(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b= b,a+b

for n in genFibo(100):
    print(n)



