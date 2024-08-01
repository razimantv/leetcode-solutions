# Power of four

[Problem link](https://leetcode.com/problems/power-of-four)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/power-of-four

class Solution {
 public:
  bool isPowerOfFour(int num) {
    return __builtin_popcount(num) == 1 and ((num & 0x55555555) == num);
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
