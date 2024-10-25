# Remove sub folders from the filesystem

[Problem link](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ret, prev = [], '$'
        for f in sorted(folder):
            if f[:len(prev) + 1] != prev + '/':
                ret.append(f)
                prev = f
        return ret
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Prefix/Suffix](/Collections/string.md#prefix-suffix)
