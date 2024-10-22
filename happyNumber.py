
def generate(number: int):
    number = str(number)
    sum1 = 0
    for i in range(len(str(number))):
        sum1 += int(number[i])**2
    return sum1

def check_happy_number(number: int):
    already = []
    result = generate(number)
    while result != 1:
        if result in already:
            return 0
        already.append(result)
        result = generate(result)
    return 1
if __name__ == '__main__':
    n = int(input())
    count = 0
    for i in range(n+1):
        if check_happy_number(i):
            print(i)
            count += 1
    print("count:", count)