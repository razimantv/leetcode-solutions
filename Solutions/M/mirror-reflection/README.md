# Mirror reflection

[Problem link](https://leetcode.com/problems/mirror-reflection)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/mirror-reflection

class Solution {
 public:
  int mirrorReflection(int p, int q) {
    if (q == 0)
      return 0;
    else if (q == p)
      return 1;

    int N = p / __gcd(p, q), M = N * q / p;
    return (N & 1) ? (M & 1) : 2;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
