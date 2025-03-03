# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left, right, cnt = [], [], 0
        for x in nums:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                cnt += 1
        return left + [pivot] * cnt + right
