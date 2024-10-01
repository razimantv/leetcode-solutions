# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter()
        for x in arr:
            x %= k
            if cnt[(k - x) % k]:
                cnt[(k - x) % k] -= 1
            else:
                cnt[x] += 1
        return not any(cnt.values())
