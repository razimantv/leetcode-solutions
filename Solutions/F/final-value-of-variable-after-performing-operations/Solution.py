# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if s[1] == '+' else -1 for s in operations)
