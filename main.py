fives = ['puton','input']
sixs = ['output']
sevens = ['inputon']
eights = ['outputon','inputone']
def valid(string):
    i = 0
    while i < len(string):
        if string[i:i+3] == 'one':
            i += 3
        elif string[i:i+9] == 'outputone':
            i += 9
        elif string[i:i+8] == 'outputon' or string[i:i+8] == 'inputone':
            i += 8
        elif string[i:i+7] == 'inputon':
            i += 7
        elif string[i:i+6] in sixs:
            i += 6
        elif string[i:i+5] in fives:
            i += 5
        elif string[i:i+3] == 'out':
            i += 3
        elif string[i:i + 2] == 'in':
            i += 2
        else:
            return False
    return True
number = int(input())
strings =[]
for i in range(number):
    strings.append(input())
for i in strings:
    if valid(i):
        print('YES')
    else:
        print('NO')