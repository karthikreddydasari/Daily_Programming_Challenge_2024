def trap(arr):
        n = len(arr)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n
        water = 0

        # Fill left array
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])

        # Fill right array
        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])

        # Calculate trapped water
        for i in range(n):
            minHeight = min(left[i], right[i])
            water += minHeight - arr[i]

        return water



arr= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(arr))
