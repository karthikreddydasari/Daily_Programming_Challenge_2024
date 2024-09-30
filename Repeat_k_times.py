def first_element_k_times(arr, k):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num in arr:
        if frequency[num] == k:
            return num

    return -1


arr = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
print(first_element_k_times(arr, k))
