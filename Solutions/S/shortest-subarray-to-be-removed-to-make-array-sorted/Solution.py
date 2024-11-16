# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        while l + 1 < n and arr[l + 1] >= arr[l]:
            l += 1
        if l == n - 1:
            return 0
        r = n - 1
        while r and arr[r - 1] <= arr[r]:
            r -= 1
        ret = r
        for i in range(l + 1):
            while r < n and arr[r] < arr[i]:
                r += 1
            ret = min(ret, r - i - 1)
        return ret
