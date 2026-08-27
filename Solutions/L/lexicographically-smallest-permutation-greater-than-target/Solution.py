# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if ''. join(sorted(s, reverse=True)) <= target:
            return ''

        chars = SortedList(s)
        ret = []
        for i, c in enumerate(target):
            if chars.count(c):
                chars.remove(c)
                if ''.join(chars[::-1]) > target[i + 1:]:
                    ret. append(c)
                    continue
                chars.add(c)
            idx = chars.bisect_right(c)
            ret.append(chars.pop(idx))
            break
        return ''. join(ret + list(chars))
