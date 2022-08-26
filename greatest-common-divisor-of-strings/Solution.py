// https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        L1, L2 = len(str1), len(str2)
        L = min(L1, L2)
        
        for x in range(L, 0, -1):
            if L1%x!=0 or L2%x!=0: continue
            candidate = str1[:x]
            
            if candidate * (L1//x) == str1 and candidate * (L2//x) == str2:
                return candidate
        
        return ""