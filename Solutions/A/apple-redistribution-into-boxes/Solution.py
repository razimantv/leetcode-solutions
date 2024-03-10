# https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        for i, x in enumerate(sorted(capacity, reverse=True)):
            tot -= x
            if tot <= 0:
                return i + 1
        return -1
