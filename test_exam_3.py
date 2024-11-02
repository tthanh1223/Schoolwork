def second_non_repeating_character(s :str) -> int:
    length = len(s)
    letters = set()
    count = 0
    index = 0
    i = -1
    while count < 2:
        if s[index] not in letters:
            letters.add(s[index])
        else:
            count += 1
            i = index
        index += 1
    return i

def able_to_palindrome(s : str) -> bool:
    letters_count = dict()
    for i in s:
        letters_count[i] = letters_count.get(i, 0) + 1
    count = 0
    for i in letters_count:
        if letters_count.get(i) % 2 == 1:
            count += 1
    return count < 2

def first_last_match(s: str) -> int:
    if len(s) == 1:
        return 0
    count = 0
    if s[0] == s[-1]: count += 1

    for i in range(0,len(s)-1):
        if s[0] == s[-1]:
            count += 1
        s = s[1:] + s[0]
    return count

def rotate90(mat):
    n = len(mat)

    # Consider all cycles one by one
    for i in range(n // 2):

        # Consider elements in group of 4
        # as P1, P2, P3 & P4 in current square
        for j in range(i, n - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = temp

def rotate_matrix(matrix,size):
    result = []
    for i in range(size):
        result.append(list(matrix[j][i] for j in range(size)))
    for i in range(size):
        result[i] = result[i][::-1]
    return result

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()



if __name__ == '__main__':
    n = int(input().strip())
    names = input().rstrip().split()
    scores = list(map(int, input().rstrip().split()))

    # Create dictionary of name:score and original position
    name_data = {}
    for i, (name, score) in enumerate(zip(names, scores)):
        name_data[name] = {'score': score, 'pos': i}

    # Sort names by scores in descending order
    sorted_names = sorted(names, key=lambda x: name_data[x]['score'], reverse=True)

    # Create ranks, handling ties
    ranks = [1]  # First rank is always 1
    for i in range(1, n):
        if name_data[sorted_names[i]]['score'] == name_data[sorted_names[i - 1]]['score']:
            ranks.append(ranks[-1])
        else:
            ranks.append(i + 1)

    # Create dictionary mapping names to ranks
    rank_dict = dict(zip(sorted_names, ranks))

    # Print ranks in original order
    for name in names:
        print(rank_dict[name], end=' ')
    # Output: 2 1 2 4 5