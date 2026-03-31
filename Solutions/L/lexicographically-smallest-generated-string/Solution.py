# https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        ret, fixed = ['a'] * (m + n - 1), [False] * (m + n - 1)
        for i, c in enumerate(str1):
            if c == 'F':
                continue
            for j in range(n):
                if fixed[i + j] and (ret[i + j] != str2[j]):
                    return ''
                fixed[i + j], ret[i + j] = True, str2[j]
        for i, c in enumerate(str1):
            if c == 'T' or any(ret[i + j] != str2[j] for j in range(n)):
                continue
            for j in range(n - 1, -1, -1):
                if not fixed[i + j] and ret[i + j] != 'z':
                    ret[i + j] = chr(ord(ret[i + j]) + 1)
                    break
            else:
                return ''
        return ''. join(ret)
