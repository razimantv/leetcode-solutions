# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ret, prev = [], '$'
        for f in sorted(folder):
            if f[:len(prev) + 1] != prev + '/':
                ret.append(f)
                prev = f
        return ret
