# Concatenation of consecutive binary numbers

[Problem link](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers

class Solution {
 public:
  int concatenatedBinary(int n) {
    int ret = 0;
    const int mod = 1'000'000'007;
    for (int i = 1, j = 2; i <= n; ++i) {
      if (i == j) j <<= 1;
      ret = (ret * (long long)j + i) % mod;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
