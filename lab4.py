

def input_matrix():
    matrix = []
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix
#takes two 2D arrays (matrices) as input and returns their sum.
def sum_matrix(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2):
        return "False rows size"
    elif len(matrix1[0]) != len(matrix2[0]):
        return "False columns size"
    else:
        rows = len(matrix1)
        cols = len(matrix1[0])
        for i in range(rows):
            result.append(list(matrix1[i][j]+matrix2[i][j] for j in range(cols)))
    return result

# find the sum of each row in a 2D array and return the results as a list
def sum_of_row(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(rows):
        result.append(sum(matrix[i]))
    return result


def input_dict():
    many = int(input("How many items: "))
    result = {}
    for i in range(many):
        key, value = input("Enter key and value (space-separated): ").split()
        result[key] = value
    return result

# take a dictionary as input and returns a new dictionary where the keys and values are swapped
def swap_dict(dictionary: dict):
    result = dict()
    for item in dictionary.items():
        result[item[1]] = item[0]
    return result

# function that finds the intersection of two sets
def intersection_of_set(set1: set, set2: set):
    result = set()
    for i in set1:
        if i in set2:
            result.add(i)
    return result

# function that returns the symmetric difference of two sets
# symmetric different means in A but not in B and in B but not in A
def symmetric_different(set1: set, set2: set):
    intersect_set = intersection_of_set(set1, set2)
    result = set()
    for i in set1:
        if i not in intersect_set:
            result.add(i)
    for i in set2:
        if i not in intersect_set:
            result.add(i)
    return result

# function to group words that are anagrams of each other using a dictionary
def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    # Dictionary to count characters in s
    count = {}
    # Count each character in s
    for char in str1:
        count[char] = count.get(char, 0) + 1
    # Decrease the count for each character in t
    for char in str2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    # If all counts are zero, they are anagrams
    return all(value == 0 for value in count.values())


def group_anagrams(words: list[str]) -> list[list[str]]:
    result = []
    for word in words:
        placed = False
        for group in result:
            if isAnagram(word, group[0]):
                group.append(word)
                placed = True
                break
        if not placed:
            result.append([word])
    return result

# Write a function that merges two nested dictionaries. If keys overlap and values
# are dictionaries, merge them recursively.
def merge_dicts(d1: dict, d2: dict) -> dict:
    merged = d1.copy()  # Start with a copy of d1 to avoid modifying it

    for key, value in d2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            # If both values are dictionaries, merge them recursively
            merged[key] = merge_dicts(merged[key], value)
        else:
            # Otherwise, set the value from d2
            merged[key] = value
    return merged

# Given a 2D array of integers, write a function that returns a dictionary where
# the keys are the unique integers and the values are their frequencies.
def count_frequencies(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    maps = dict()
    for i in range(rows):
        for j in range(cols):
            maps[matrix[i][j]] = maps.get(matrix[i][j], 0) + 1
    return maps

# Given two sets, write a Python function to find the elements present in the first
# set but not in the second.
def just_set1(s1: set, s2: set) -> set:
    result = set()
    for i in s1:
        if i not in s2:
            result.add(i)
    return result

# Write a function to find common elements among all rows of a 2D array, where
# each row is treated as a tuple.
def common_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    commons = set(matrix[0])
    for i in range(1,rows):
        commons = intersection_of_set(commons, matrix[i])
    return commons if commons else {}


def is_sorted(words, order):
    # Map each character in the custom order to its index
    order_map = {char: idx for idx, char in enumerate(order)}

    # Function to convert a word to its custom order indices
    def to_custom_order(word):
        return [order_map[char] for char in word]

    # Check each pair of consecutive words
    for i in range(len(words) - 1):
        # Compare each word's custom order representation
        if to_custom_order(words[i]) > to_custom_order(words[i + 1]):
            return False

    return True


if __name__ == "__main__":
    words = ["hellpzzo", "intelligent", "llass"]
    order = "hlabicdefgjkmnopqrstuvwxyz"
    print(is_sorted(words, order))  # Output: True
