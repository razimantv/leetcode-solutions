# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k and stack[-1] > c:
                stack.pop()
                k -= 1
            stack. append(c)
        while k:
            stack.pop()
            k -= 1

        for i, c in enumerate(stack):
            if c > '0':
                return ''. join(stack[i:])
        return '0'
