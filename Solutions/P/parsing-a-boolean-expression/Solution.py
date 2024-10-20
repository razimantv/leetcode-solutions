# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack, match = [], {}
        for i, c in enumerate(expression):
            if c == '(':
                stack.append(i)
            elif c ==')':
                match [stack. pop()] = i
                
        def work(l, r):
            if l == r:
                return expression[l] == 't'
            elif expression[l] == '!':
                return not work(l + 2, r - 1)
            
            pos = l + 2
            while pos < r:
                if expression[pos] in 'ft':
                    cur = work(pos, pos)
                    pos += 2
                else: 
                    cur = work(pos, match[pos + 1])
                    pos = match[pos + 1] + 2
                if (expression[l] == '|') == cur:
                    return cur
            return expression[l] == '&'
        
        return work(0, len(expression) - 1)
