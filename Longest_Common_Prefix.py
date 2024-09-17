def longest_common_prefix(arr):
    result = []
    for i in range(len(arr[0])):
        prefix = arr[0][i]
        for j in arr[1:]:
            if i >= len(j) or j[i] != prefix:
                return '"' + "".join(result) + '"'

        result.append(prefix)

    return '"' + "".join(result) + '"'

arr =  ["flower","flow","flight"]
print(longest_common_prefix(arr))
