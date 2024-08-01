# Hamming distance

[Problem link](https://leetcode.com/problems/hamming-distance)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/hamming-distance

class Solution {
 public:
  int hammingDistance(int x, int y) { return __builtin_popcount(x ^ y); }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
