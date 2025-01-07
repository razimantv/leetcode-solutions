# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret, words = [], sorted(words, key=len)
        for i, x in enumerate(words):
            for y in words[i + 1:]:
                if y. find(x) != -1:
                    ret. append(x)
                    break
        return ret
