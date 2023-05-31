# Number of common factors

[Problem link](https://leetcode.com/problems/number-of-common-factors/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-common-factors/

class Solution {
 public:
  int commonFactors(int a, int b) {
    int g = __gcd(a, b), ret = 0;
    for (int i = 1; i <= g; ++i)
      if (g % i == 0) ++ret;
    return ret;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
