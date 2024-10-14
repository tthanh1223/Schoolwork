# sàng nguyên tố - sieve of prime
# lan tới đâu
def sieve_prime(n:int):
    char = [True] * (n+1)
    i = 2
    while i **2 <= n:
        if char[i]:
            l = i**2
            while l <= n:
                char[l] = False
                l += i
        i += 1
    for i in range(2,n+1):
        if char[i]:
            print(i,end=' ')

sieve_prime(10000)
list(range(1,100)).sort()