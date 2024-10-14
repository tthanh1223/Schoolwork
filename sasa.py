def find_all_indices(a: list, n: int) -> list:
    indices = []
    for i in range(len(a)):
        if a[i] == n:
            indices.append(i)
    return indices

def is_prime(n:int):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def get_prime_list(n:int) -> list:
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def check_ascend(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] > nums[i + 1]  :
            return False
    return True

print(check_ascend([1,2,3,2]))
# check step for repeatedly ascending