# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ret = [""]
        for c in target:
            ret += [
                ret[-1] + chr(ord('a') + x)
                for x in range(ord(c) - ord('a') + 1)
            ]
        return ret[1:]
