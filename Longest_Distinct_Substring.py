def longest_substring_without_repeating(s):
    start = 0
    max_length = 0
    used_chars = {}

    for i in range(len(s)):
        if s[i] in used_chars and used_chars[s[i]] >= start:
            start = used_chars[s[i]] + 1
        used_chars[s[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage:
print(longest_substring_without_repeating("abcabcbb"))  # Output: 3
print(longest_substring_without_repeating("bbbbb"))     # Output: 1
print(longest_substring_without_repeating("pwwkew"))    # Output: 3
