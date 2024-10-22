import random


def highest_frequency(points: list[int]):
    counts = []
    marks = []
    for i in points:
        if i not in marks:
            marks.append(i)
            counts.append(1)
        else:
            counts[marks.index(i)] += 1
    max_count = max(counts)
    result = list()
    for i in range(len(marks)):
        if counts[i] == max_count:
            result.append(marks[i])
    return result
# the maximum number of consecutive students with score >= 50
def maximum_number_students_above_average(points: list[int]):
    max1 = 0
    count = 0
    best_start = 0
    current_start = 0
    for i,score in enumerate(points):
        if score >= 50:
            if count == 0:
                current_start = i
            count += 1
            if count > max1:
                max1 = count
                best_start = current_start
        else:
            count = 0
    subs = points[best_start:best_start+max1]
    return max1, subs

if __name__ == '__main__':
    test_points = [random.randint(0, 100) for _ in range(100)]
    print(maximum_number_students_above_average(test_points))