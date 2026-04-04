# https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution:
    def decodeCiphertext(self, text: str, r: int) -> str:
        if r == 1 or not text:
            return text

        m, ret = len(text) // r, []
        for i in range(m):
            for j in range(r):
                if i + j < m:
                    ret.append(text[j * m + i + j])

        while ret[-1] == ' ':
            ret.pop(-1)
        return ''. join(ret)
