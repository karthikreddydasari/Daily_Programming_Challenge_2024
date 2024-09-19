def recur_permute(index, nums, ans):
    if index == len(nums):
        ans.append(nums[:])
        return
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        recur_permute(index + 1, nums, ans)
        nums[index], nums[i] = nums[i], nums[index]

def permute(nums):
    ans = []
    recur_permute(0, nums, ans)
    return ans


v = [1, 2, 3, 4]
result = permute(v)

for perm in result:
    print(" ".join(str(x) for x in perm))
