#!/bin/python3

import os
from typing import Any


#
# Complete the 'findSubstring' function below.
#aa
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def vowel_check(c):
    return c in 'aueio'
def findSubstring(string, length):
    # Write your code here
    if len(string) < length:
        return 'Not found!'
    current_vowel_count = sum(1 for i in range(length) if vowel_check(string[i]))
    final_subtring: str | Any = string[:length] if current_vowel_count > 0 else "Not found!"
    max_vowel_count = current_vowel_count
    for i in range(1, len(string) - length + 1):
        if vowel_check(string[i - 1]):
            current_vowel_count -= 1
        if vowel_check(string[i + length - 1]):
            current_vowel_count += 1
        substring = string[i:i + length]
        if current_vowel_count > max_vowel_count:
            max_vowel_count = current_vowel_count
            final_subtring = substring
    return final_subtring
# complexity time is O(n.k), we need to find a way to just O(n)
# here we use sliding method for better runtime

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
