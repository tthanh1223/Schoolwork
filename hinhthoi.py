# rows : 4
#1.       *
#2.     * * *
#3.   * * * * *
#4. * * * * * * *
#5.   * * * * *
#6.     * * *
#7.       *
# 1 = a5 + 4b
  #2 = a6 + 4b
a= 1
b = -1
def print_hinh_thoi(number:int):
    for i in range(1,2*number,1):
        if i < number:
            for j in range(1,2*number,1):
                if j < number - i + 1:
                    print("   ",end ='')
                elif number-i+1 <= j <= number + i -1:
                    print("*  ",end ='')
        elif i == number:
            for j in range(2*number - 1):
                print("*  ",end ='')
        if i > number:
            for j in range(1,2*number,1):
                if j < i - number+ 1:
                    print("   ",end ='')
                elif i - number + 1 <= j <= 2*number - (i - number + 1 ):
                    print("*  ",end ='')
        print()
number = int(input("Number of rows: "))
print_hinh_thoi(number)
