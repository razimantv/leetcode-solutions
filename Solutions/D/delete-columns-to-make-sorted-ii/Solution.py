# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n, ret = len(strs), 0
        todo = [(i, i - 1) for i in range(1, n)]
        for i in range(len(strs[0])):
            if any(strs[a][i] < strs[b][i] for a, b in todo):
                ret += 1
            else:
                todo = [(a, b) for (a, b) in todo if strs[a][i] == strs[b][i]]
        return ret
