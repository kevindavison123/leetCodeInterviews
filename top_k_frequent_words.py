def findTopKFrequentWords(words, k):
    results = {}
    for word in words:
        if results.get(word):
            occurance = results[word]
            results[word] = occurance + 1
        else:
            results[word] = 1
    sorted_words = sorted(results.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_words)
    print(converted_dict)
    keys = converted_dict.keys()
    return list(keys)[:k]

if __name__ == '__main__':
    arr = ["i","love","leetcode","i","love","coding"]
    print(findTopKFrequentWords(arr,2))