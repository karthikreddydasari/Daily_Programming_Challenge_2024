def reverse_words(str):
    result = str.split()
    result = result[::-1]
    return '"' + " ".join(result) + '"'


str = "My name is Blue"
print(reverse_words(str))
