def Find_Missing(arr):
    for i in range(1,len(arr)+1):
        if i!=arr[i-1]:
           return i
    return len(arr)+1

arr= [1,2,4,5]
print(Find_Missing(arr))
arr=[2, 3, 4, 5]
print(Find_Missing(arr))
arr=[1, 2, 3, 4]
print(Find_Missing(arr))
arr=[1]
print(Find_Missing(arr))
