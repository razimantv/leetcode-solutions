# https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        cnt = [0] * 30
        ret, l = 1 << 31, 0
        for r, x in enumerate(nums):
            cur = 0
            for i in range(30):
                if not (x & (1 << i)):
                    cnt[i] += 1
                if not cnt[i]:
                    cur |= 1 << i
            ret = min(ret, abs(k - cur))
            while cur < k:
                cur = 0
                for i in range(30):
                    if not (nums[l] & (1 << i)):
                        cnt[i] -= 1
                    if not cnt[i]:
                        cur |= 1 << i
                l += 1
                if l <= r:
                    ret = min(ret, abs(k - cur))
        return ret
