# Bitwise and of numbers range

[Problem link](https://leetcode.com/problems/bitwise-and-of-numbers-range)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution {
 public:
  int rangeBitwiseAnd(int m, int n) {
    int ret = 0;
    for (int i = 30; i >= 0; --i) {
      if ((m & (1 << i)) == (n & (1 << i)))
        ret |= (m & (1 << i));
      else
        break;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
