def subarrays_sum_zero(arr):
    result = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum == 0:
                result.append((i, j))
    return result


arr = [1, 2, -3, 3, -1, 2]
print(subarrays_sum_zero(arr))
