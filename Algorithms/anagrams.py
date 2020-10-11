from pprint import pprint

words = [] # list container
with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.append(w)

# print(words[-10:])


'''
words = {}
with open("words.txt") as f:
    for w in f:
        w = w.strip()
        l = len(w)
        if l not in words:
            words[l] = []
        words[l].append(w)

# print(words[8])
# import sys; sys.exit()
'''

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


# print(sorted(words.keys()))


def anagrams():
    '''
    for word1 in words: # O(n^2)
        for word2 in words:
            if word1 == word2:
                continue
            if is_anagram(word1, word2):
                print(word1, word2)
    
    for wordlen in range(10, 21):
        if wordlen == 19: continue
        for word1 in words[wordlen]:  # O(n^2)
            for word2 in words[wordlen]:
                if word1 == word2:
                    continue
                if is_anagram(word1, word2):
                    print(word1, word2)
    '''
    result = {}
    results_by_len = {}
    longest_sig = None
    longest_len = -1

    for w in words: # O(n) over the number of word
        signature = ''.join(sorted(w))

        if signature not in result:
            result[signature] = []
        result[signature].append(w)

        if len(result[signature]) > longest_len:
            longest_len = len(result[signature])
            longest_sig = signature
    '''
    for sig in result: # O(n) over the number of sigs
        l = len(result[sig])
        if l not in results_by_len:
            results_by_len[l] = []
        results_by_len[l].append(result[sig])
    
    for i in range(5,9):
        try:
            pprint(results_by_len[i])
        except:
            pass
    '''
    return result[longest_sig]

pprint(anagrams()) 
