# https://leetcode.com/problems/brace-expansion-ii/


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def match(l):
            cnt = 1
            while cnt:
                l += 1
                if expression[l] == "{":
                    cnt += 1
                elif expression[l] == "}":
                    cnt -= 1
            return l

        def work(l, r):
            if l == r:
                return set(expression(l))
            ret, cur, idx = set(), {""}, l
            while idx <= r:
                if expression[idx] == ",":
                    ret.update(cur)
                    cur = {""}
                else:
                    if expression[idx] == "{":
                        m = match(idx)
                        add = work(idx + 1, m - 1)
                        idx = m
                    else:
                        add = set(expression[idx])
                    cur = {x + y for x in cur for y in add}
                idx += 1
            ret.update(cur)
            return ret

        return sorted(work(0, len(expression) - 1))
