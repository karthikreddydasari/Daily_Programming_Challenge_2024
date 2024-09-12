def merge_sorted(arr1, arr2, m, n):
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]

            arr2.sort()

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge_sorted(arr1, arr2, len(arr1), len(arr2))
print("arr1:", arr1)#[1,2,3]
print("arr2:", arr2)#[4,5,6]
