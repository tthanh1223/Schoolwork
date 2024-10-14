def find_missing_value(points:list[int]):
    n = len(points)
    if n >= 3:
        for i in range(n):
            if points[i] == -1:
                if i == 0:
                   points[i] = 2*points[i+1] - points[i+2] if 2*points[i+1] - points[i+2] >= 0 else -1
                   return 1
                elif i == n - 1:
                    points[i] = 2*points[i-1] - points[i-2] if 2*points[i-1] - points[i-2] <= 100 else -1
                    return 1
                else:
                    points[i] = (points[i - 1] + points[i + 1]) / 2
    else:
        print("Not enough data")
        return 0
def is_ascending(nums):
    if len(nums) == 1 or len(nums) == 2:
        return True
    for i in range(1,len(nums)-1):
        if nums[i+1] - nums[i] == nums[i] - nums[i-1] and nums[i-1] < nums[i] < nums[i+1]:
            return True
    return False

def find_max_list(sales:list):
    steps = []
    result = []
    for i in range(0,len(sales)-1):
        steps.append(sales[i+1]-sales[i])
        if is_ascending(steps):
            result.append(sales[i])
        else:
            continue
    return result

input_data = input().split()
print(input_data)
