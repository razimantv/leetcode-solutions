# https://leetcode.com/problems/maximum-frequency-after-subarray-operation

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        ctr = Counter(nums)

        def work(t, k):
            ret, cur, best = 0, 0, 0
            for x in nums:
                cur += 1 if x == t - k else -1 if x == t else 0
                ret = max(ret, cur - best)
                best = min(best, cur)
            return ret

        return max(ctr[k] + work(k, d) for d in range(k - 50, k) if d)
