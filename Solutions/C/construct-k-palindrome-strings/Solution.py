# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(x & 1 for x in Counter(s).values()) <= k
