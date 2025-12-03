def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = find_max(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max

print(find_max([5, 2, 9, 1, 5, 6]))