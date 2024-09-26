
def count_divisors(num):
    count=0
    for i in range(1, num+1):
        if num%i ==0:
            count=count+1

    return count

num=18
print(count_divisors(num))
