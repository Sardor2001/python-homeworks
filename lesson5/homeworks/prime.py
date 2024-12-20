def is_prime(n):
    s = 0
    for i in range(1, n):
        if n%i==0:
            s+=1
    if s==1:
        return True
    return False

n = int(input("Enter a number: "))
print(is_prime(n))
