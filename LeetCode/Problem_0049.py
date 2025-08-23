# LeetCode Problem 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram[sorted_word].append(word)
        return list(anagram.values())

    # charecter = []
    # anagram = []
    # for word in strs:
    #     cha = defaultdict(int)
    #     for ch in word:
    #         cha[ch] += 1
    #     if cha not in charecter:
    #         charecter.append(cha)
    #         anagram.append([word])
    #     else:
    #         anagram[charecter.index(cha)].append(word)
    # return anagram
