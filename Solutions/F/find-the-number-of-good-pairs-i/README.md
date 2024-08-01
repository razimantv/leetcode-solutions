# Find the number of good pairs i

[Problem link](https://leetcode.com/problems/find-the-number-of-good-pairs-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = max(nums1)
        sieve = [0] * (n + 1)
        for x, c in Counter(nums2). items():
            y = x * k
            for z in range(y, n + 1, y):
                sieve[z] += c
        return sum(sieve[x] for x in nums1)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
