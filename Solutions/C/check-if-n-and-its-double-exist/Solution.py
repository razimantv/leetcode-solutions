# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = Counter(arr)
        for k, v in list(seen. items()):
            if seen[2 * k] > (k == 0):
                return True
        return False
