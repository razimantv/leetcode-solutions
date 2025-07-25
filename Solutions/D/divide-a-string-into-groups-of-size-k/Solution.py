# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        n = len(s)
        if n % k:
            s += fill * (k - n % k)
        n = len(s)
        return [s[i:i + k] for i in range(0, n, k)]
