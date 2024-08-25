# Count almost equal pairs ii

[Problem link](https://leetcode.com/problems/count-almost-equal-pairs-ii/)

## Solutions


### Solution.cpp
```cpp
# https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        d = len(str(max(nums)))
        cnt = Counter(nums)
        ret = sum(v * (v - 1) // 2 for v in cnt.values())
        
        transform = defaultdict(list)
        for x in cnt: 
            transform[x].append(x)
            s = list(str(x).zfill(d))
            for i in range(d): 
                for j in range(i): 
                    if s[i] == s[j]:
                        continue
                    s[i], s[j] = s[j], s[i]
                    y = int("".join(s))
                    transform[y].append(x)
                    s[i], s[j] = s[j], s[i]
        
        pairs = set() 
        for y, xvec in transform.items():
            for x1, x2 in combinations(xvec, 2): 
                pairs.add((min(x1, x2), max(x1, x2)))
        for x1, x2 in pairs:
            ret += cnt[x1] * cnt[x2]
        return ret
```
### Solution.py
```py
# https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        d = len(str(max(nums)))
        cnt = Counter(nums)
        ret = sum(v * (v - 1) // 2 for v in cnt.values())

        transform = defaultdict(list)
        for x in cnt:
            transform[x].append(x)
            s = list(str(x).zfill(d))
            for i in range(d):
                for j in range(i):
                    if s[i] == s[j]:
                        continue
                    s[i], s[j] = s[j], s[i]
                    y = int("".join(s))
                    transform[y].append(x)
                    s[i], s[j] = s[j], s[i]

        pairs = set()
        for y, xvec in transform.items():
            for x1, x2 in combinations(xvec, 2):
                pairs.add((min(x1, x2), max(x1, x2)))
        for x1, x2 in pairs:
            ret += cnt[x1] * cnt[x2]
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
* [Meet in the middle](/Collections/meet-in-the-middle.md#meet-in-the-middle)
