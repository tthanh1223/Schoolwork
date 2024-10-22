def rotate_array(arr: list, step: int):
    num = 0
    index = 0
    while num < step:
        arr.insert(0,arr.pop())
        num += 1
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate_array(arr, 2))
