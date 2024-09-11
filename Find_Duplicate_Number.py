def Find_Duplicate_Number(arr):
    n=len(arr)-1
    without_duplicate_sum=n*(n+1)//2
    given_sum = sum(arr)

    return given_sum-without_duplicate_sum

arr= [1, 3, 4, 2, 2]
print(Find_Duplicate_Number(arr))#2
arr=[3, 1, 3, 4, 2]
print(Find_Duplicate_Number(arr))#3
arr=[1, 1]
print(Find_Duplicate_Number(arr))#1
arr=[1, 4, 4, 2, 3]
print(Find_Duplicate_Number(arr))#4
