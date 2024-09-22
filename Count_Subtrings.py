s = "pqpqs"
k = 2


def at_most_k_distinct(s, k):
    count = {}
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        result += right - left + 1

    return result


count_at_most_k = at_most_k_distinct(s, k)
count_at_most_k_minus_1 = at_most_k_distinct(s, k - 1)
exactly_k_distinct = count_at_most_k - count_at_most_k_minus_1

print(exactly_k_distinct)
