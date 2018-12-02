# https://adventofcode.com/2018/day/2

from collections import Counter

def common(word1, word2):
    return ''.join([i for i, j in zip(word1, word2) if i == j])

with open('2.txt', 'r') as f:
    words = f.readlines()
    has_appears_twice = 0
    has_appears_thrice = 0
    for word in words:
        found_twice = False
        found_thrice = False
        counts = Counter(word)
        for letter, count in counts.items():
            if count == 2 and not found_twice:
                has_appears_twice += 1
                found_twice = True
            elif count == 3 and not found_thrice:
                has_appears_thrice += 1
                found_thrice = True
    print(has_appears_twice * has_appears_thrice)

    nbrs = {}
    for word_idx, word in enumerate(words):
        if word in nbrs:
            print(common(word, words[nbrs[word]]))
            break
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                nbrs[word[:i] + char + word[i+1:]] = word_idx