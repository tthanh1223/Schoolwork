# read all the file and print all its contents to the screen
def read_file(fname:str):
    with open(fname, 'r') as f:
        a = f.read()
    return a

# read the first n lines of the file and print them to the screen
def read_lines(fname:str, number:int):
    with open(fname, 'r') as f:
        a = f.readlines()
    for i in a:
        if i == '\n':
            a.remove(i)
    for i in range(number-1):
        print(a[i],end='')

# read the last n lines of the file and print them
def read_last_lines(fname:str, number:int):
    with open(fname, 'r') as f:
        a = f.readlines()
    for i in range(len(a)-1,len(a)-number,-1):
        print(a[i],end='')

# search for the longest strings in the file
def find_longest(fname:str):
    with open(fname, 'r') as f:
        a = f.readlines()
    max_len = 0
    word = ''
    for line in a:
        line = line.replace(', ',' ')
        line = line.strip().split()
        for i in range(len(line)):
            if len(line[i]) > max_len:
                max_len = len(line[i])
                word = line[i]
    return word

# shortest string
def find_shortest(fname:str):
    with open(fname, 'r') as f:
        a = f.readlines()
    max_len = 200
    word = ''
    for line in a:
        line = line.replace(', ',' ')
        line = line.strip().split()
        for i in range(len(line)):
            if len(line[i]) < max_len:
                max_len = len(line[i])
                word = line[i]
    return word

# count the number of lines
def count_lines(fname:str):
    with open(fname, 'r') as f:
        a = f.readlines()
    return len(a)

def count_words(fname:str):
    words = []
    counts = []
    with open(fname, 'r') as f:
        text = f.read().lower()
    for char in '.,!?;:':
        text = text.replace(char, ' ')
    word_list = text.split()
    for word in word_list:
        if word in words:
            index = words.index(word)
            counts[index] += 1
        else:
            words.append(word)
            counts.append(1)
    return words, counts


# count the occurrences of each letter in the file
def count_letters(fname:str):
    with open(fname, 'r') as f:
        text = f.read().lower()
    counts = [0] * 26
    for char in text:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            counts[index] += 1
    for i in range(26):
        print(f"{chr(i+ord('a'))}: {counts[i]}")

# words appear the most in file
def words_most(fname: str):
    words, counts = count_words(fname)
    max_count = max(counts)

    # Find all words that have the maximum count.
    most_frequent_words = [words[i] for i in range(len(words)) if counts[i] == max_count]

    return most_frequent_words

def words_least(fname: str):
    words, counts = count_words(fname)
    min_count = min(counts)
    least_frequent_words = [words[i] for i in range(len(words)) if counts[i] == min_count]
    return least_frequent_words

def word_end_with(fname: str, letter:str):
    words, counts = count_words(fname)
    result = []
    for word in words:
        if word.endswith(letter):
            result.append(word)
    return result

# give n and k ,write a function to return the words that appear between n and k times in the file
def between_n_and_k_times(fname:str,n:int,k:int):
    words, counts = count_words(fname)
    result =[]
    for i in range(len(words)):
        if n <= counts[i] < k:
            result.append(words[i])
    return result

# Write a function to copy the lines from n to k of the file "text.txt" and paste
# them into a new file. Name the new file "output.txt".
def copy_lines_between_n_and_k(fname: str, n: int, k: int):
    lines = []
    with open(fname, 'r') as f:
        a = f.readlines()
        for i in range(n,k+1):
            lines.append(a[i])
    with open('output.txt','w') as f:
        for line in lines:
            f.write(line)

# returns the words that most frequently appear immediately before a given word in a text file
def before_given_word_most(fname: str, target: str):
    with open(fname, 'r') as f:
        text = f.read()
    for char in '.,!?;:':
        text = text.replace(char, ' ')
    word_list = text.split()
    words = []
    counts = []
    for i in range(1,len(word_list)):
        if word_list[i] == target:
            if word_list[i-1] in words:
                counts[words.index(word_list[i-1])] += 1
            else:
                words.append(word_list[i-1])
                counts.append(1)
    max_count = max(counts)
    return list(words[i] for i in range(len(words)) if counts[i] == max_count) if not None else []

# return the lines that contain a given word. If none is found, return None.
def lines_contain_word(fname:str, word:str):
    lines = []
    with open(fname, 'r') as f:
        text = f.readlines()

    for line in text:
        if word in line:
            lines.append(line)
    return lines if lines else []

# Write a function to replace a word or a string in the file with another word or string.
def replace_word_in_file(fname: str, old_word: str, new_word: str):
    with open(fname, 'r') as f:
        text = f.read()

    # Replace the old word with the new word.
    updated_text = text.replace(old_word, new_word)

    with open(fname, 'w') as f:
        f.write(updated_text)

# Write a function to insert any content into the file at a given line number n.
def insert_content_at_line(fname: str, content: str, line_num: int):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Adjusting for zero-based indexing.
    line_num -= 1
    if line_num < 0:
        line_num = 0
    elif line_num > len(lines):
        line_num = len(lines)

    # Insert the content at the specified line number.
    lines.insert(line_num, content + '\n')

    with open(fname, 'w') as f:
        f.writelines(lines)

def delete_line(fname: str, line_num: int):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Adjusting for zero-based indexing.
    line_num -= 1
    if 0 <= line_num < len(lines):
        del lines[line_num]

    with open(fname, 'w') as f:
        f.writelines(lines)

def write_array_to_file(array):
    with open('output2.txt', 'w') as f:
        for element in array:
            f.write(str(element) + '\n')


def number_to_words(n):
    # Define word representations for numbers
    ones = (
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    )
    tens = (
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    )
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + " hundred" + ('' if n % 100 == 0 else ' and ' + number_to_words(n % 100))
    elif n < 1000000:
        return number_to_words(n // 1000) + " thousand" + ('' if n % 1000 == 0 else ' ' + number_to_words(n % 1000))


def convert_numbers_to_words(fname: str):
    with open(fname, 'r') as f:
        text = f.read()
    words = text.split()
    updated_words = []
    for word in words:
        if word.isdigit():
            word = number_to_words(int(word))
        updated_words.append(word)
    updated_text = ' '.join(updated_words)
    with open(fname, 'w') as f:
        f.write(updated_text)


if __name__ == '__main__':
    fname = 'text.txt'
    convert_numbers_to_words(fname)