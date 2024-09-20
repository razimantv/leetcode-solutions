# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        funcs = {'+': add, '-': sub, '*': mul}

        @cache
        def work(i, j):
            ret = []
            for k in range(i + 1, j - 1):
                if expression[k] in '+-*':
                    ret.extend([
                        funcs[expression[k]](x, y)
                        for x, y in product(work(i, k), work(k + 1, j))
                    ])
            if not ret:
                ret.append(int(expression[i:j]))
            return ret
        return work(0, len(expression))
