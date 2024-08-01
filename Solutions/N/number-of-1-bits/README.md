# Number of 1 bits

[Problem link](https://leetcode.com/problems/number-of-1-bits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-1-bits

class Solution {
 public:
  int hammingWeight(uint32_t n) { return __builtin_popcount(n); }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
