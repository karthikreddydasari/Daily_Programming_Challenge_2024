def find_anagrams(words):
    answer = []
    for i in range(len(words)):
        result = []
        for j in range(len(words)):
            if sorted(words[i]) == sorted(words[j]):
                if words[j] not in result:
                    result.append(words[j])

        if result not in answer:
            answer.append(result)

    return answer


words = ["eat", "ate", "tea", "bat", "tan", "nat"]
print(find_anagrams(words))
