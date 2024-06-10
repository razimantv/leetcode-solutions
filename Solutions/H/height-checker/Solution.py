# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([1 for h, j in zip(heights, sorted(heights)) if h != j])
