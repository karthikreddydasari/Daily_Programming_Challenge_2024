def Sort_0_1_2_array(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    for num in arr:
        if num==0:
            count0=count0+1
        elif num==1:
            count1=count1+ 1
        elif num==2:
            count2=count2+1
    i=0
    for _ in range(count0):
        arr[i]=0
        i+=1
    for _ in range(count1):
        arr[i] = 1
        i+=1
    for _ in range(count2):
        arr[i] = 2
        i+=1
    print(arr)


arr = [0, 1, 2, 1, 0, 2, 1, 0]
Sort_0_1_2_array(arr)
arr= [2, 2, 2, 2]
Sort_0_1_2_array(arr)
arr= [0, 0, 0, 0]
Sort_0_1_2_array(arr)
arr= [1, 1, 1, 1]
Sort_0_1_2_array(arr)
arr=[2, 0, 1]
Sort_0_1_2_array(arr)
arr=[]
Sort_0_1_2_array(arr)
