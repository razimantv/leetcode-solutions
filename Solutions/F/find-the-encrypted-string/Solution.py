# https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        return ''.join([s[(i + k) % n] for i in range(n)])
