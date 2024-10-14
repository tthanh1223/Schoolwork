'''
3 non-negative integer a ,b,c. Arrange them in some order and put + - x sign between them to minimize the outcome of the resulting
not expression
No ()
exactly one sign between every pair of neighboring numbers.'''

def minimize_outcome(a :int, b :int, c :int):
    result = [a + b - c, a + b * c, a + b + c, a - b + c, a - b - c, a - b * c, a * b * c, a * b + c, a * b - c]
    return min(result)
a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = int(input("Enter number3:"))
if a < 0 or b < 0 or c < 0:
    print("Invalid input")
print(minimize_outcome(a,b,c))

#hàm để đọc string viết ra thành chữ
#hàm để tự insert operator vào giữa các số


