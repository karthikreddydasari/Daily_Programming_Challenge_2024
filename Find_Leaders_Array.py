def find_leaders(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:
                break
        else:
            result.append(arr[i])
    return result


arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))
