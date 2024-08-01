# Minimum cuts to divide a circle

[Problem link](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution {
 public:
  int numberOfCuts(int n) {
    if (n == 1)
      return 0;
    else if (n & 1)
      return n;
    else
      return n / 2;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
