# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ret = []
        for word in words:
            if not ret or sorted(ret[-1]) != sorted(word):
                ret. append(word)
        return ret
