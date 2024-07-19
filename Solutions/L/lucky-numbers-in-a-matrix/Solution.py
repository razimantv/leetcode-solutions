# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return set(map(min, matrix)) & set(map(max, zip(*matrix)))
