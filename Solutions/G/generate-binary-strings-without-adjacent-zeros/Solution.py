# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        prev = self.validStrings(n - 1)
        return [s + "1" for s in prev] + [
            s + "0" for s in prev if s[-1] == '1'
        ]
