# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        target = (n * (n + 1) // 2 + 1) // 2

        def work(k):
            l, cnt = 0, 0
            seen = defaultdict(int)
            for r in range(n):
                seen[nums[r]] += 1
                while len(seen) > k:
                    seen[nums[l]] -= 1
                    if seen[nums[l]] == 0:
                        seen.pop(nums[l])
                    l += 1
                cnt += r - l + 1
                if cnt >= target:
                    return True
            return False

        start, end = 0, n
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                end = mid
            else:
                start = mid
        return end
