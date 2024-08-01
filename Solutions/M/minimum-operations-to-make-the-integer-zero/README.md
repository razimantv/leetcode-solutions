# Minimum operations to make the integer zero

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
 public:
  int makeTheIntegerZero(int num1, int num2) {
    long long remaining{num1};
    for (int i = 1; i < 63; ++i) {
      if ((remaining -= num2) < i) return -1;
      if (__builtin_popcountll(remaining) <= i) return i;
    }
    return -1;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
