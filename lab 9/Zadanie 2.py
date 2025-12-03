def find_min(arr, n):
    if n == 1:
        return arr[0]
    else:
        return min(arr[n-1], find_min(arr, n-1))

arr = [4, 7, 2, 9, 1, 5]
result = find_min(arr, len(arr))
print("Минимальный элемент:", result)