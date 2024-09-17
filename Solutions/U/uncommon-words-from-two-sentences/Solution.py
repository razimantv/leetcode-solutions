# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [
            word
            for word, count in Counter((s1 + ' ' + s2).split(' ')).items()
            if count == 1
        ]
