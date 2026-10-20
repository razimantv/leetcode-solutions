# https://leetcode.com/problems/sum-of-sortable-integers/


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def sortable(l, r):
            a = b = nums[l]
            flip = False
            for i in range(l + 1, r):
                if nums[i] < nums[i - 1]:
                    if flip:
                        return None, None
                    flip = True
                if flip and nums[i] > nums[l]:
                    return None, None
                a = min(a, nums[i])
                b = max(b, nums[i])
            return a, b

        def k_sortable(k):
            prev = -inf
            for l in range(0, n, k):
                a, b = sortable(l, l + k)
                if a is None or a < prev:
                    return False
                prev = b
            return True

        i, ret = 1, 0
        while i * i <= n:
            if n % i == 0:
                if k_sortable(i):
                    ret += i
                if i * i < n and k_sortable(n // i):
                    ret += n // i
            i += 1
        return ret
