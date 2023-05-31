# Broken calculator

[Problem link](https://leetcode.com/problems/broken-calculator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/broken-calculator

class Solution {
 public:
  int brokenCalc(int X, int Y) {
    int ret = 0;
    while (Y > X) {
      if (Y & 1)
        ++Y;
      else
        Y >>= 1;
      ++ret;
    }
    return ret + X - Y;
  }
};
```