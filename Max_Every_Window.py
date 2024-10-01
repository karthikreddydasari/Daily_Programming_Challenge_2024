def max_every_window(arr,k):
    result=[]
    for i in range(0,len(arr)-k+1):
        sub_arr = []
        for j in range(i,i+k):
            sub_arr.append(arr[j])
        max_element = max(sub_arr)
        result.append(max_element)
    return result


arr = [7, 7, 7, 7]
k = 1
print(max_every_window(arr,k))