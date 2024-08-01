# Divide two integers

[Problem link](https://leetcode.com/problems/divide-two-integers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/divide-two-integers

class Solution {
 public:
  int divide(int dividend, int divisor) {
    if (divisor == 1)
      return dividend;
    else if (dividend == INT_MIN and divisor == -1)
      return INT_MAX;
    else if (divisor == INT_MIN)
      return dividend == INT_MIN;

    int fac = 1, ret = 0;
    if (divisor < 0) divisor = -divisor, fac = -fac;
    if (dividend < 0) {
      if (dividend == INT_MIN) ++ret, dividend += divisor;
      dividend = -dividend;
      fac = -fac;
    }

    int p = 0;
    while ((divisor << p) <= (dividend >> 1)) ++p;
    while (p >= 0) {
      if ((divisor << p) <= dividend)
        ret += (1 << p), dividend -= (divisor << p);
      --p;
    }
    return fac == -1 ? -ret : ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
