# Power of two

[Problem link](https://leetcode.com/problems/power-of-two)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/power-of-two

class Solution {
 public:
  bool isPowerOfTwo(int n) { return n > 0 and !(n & (n - 1)); }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
