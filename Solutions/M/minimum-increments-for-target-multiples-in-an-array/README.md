# Minimum increments for target multiples in an array

[Problem link](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

class Solution:
    def minimumIncrements(self, nums: list[int], target: list[int]) -> int:
        n = len(target)
        maxmask = 1 << n
        lcm = [1] * maxmask
        for i in range(maxmask):
            for j in range(4):
                if i & (1 << j):
                    lcm[i] = (lcm[i] * target[j]) // gcd(lcm[i], target[j])

        dp = [0] + [math.inf] * (maxmask - 1)
        for x in nums:
            add = [y - x % y if x % y else 0 for y in lcm]
            newdp = deepcopy(dp)
            for oldmask in range(maxmask):
                for curmask in range(maxmask):
                    newmask = oldmask | curmask
                    newdp[newmask] = min(
                        newdp[newmask], dp[oldmask] + add[curmask]
                    )
            dp = newdp
        return dp[-1]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Subset enumeration](/Collections/bitwise-operation.md#subset-enumeration)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [GCD/LCM](/Collections/mathematics.md#gcd-lcm)
