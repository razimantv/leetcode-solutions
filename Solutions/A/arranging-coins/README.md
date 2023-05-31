# Arranging coins

[Problem link](https://leetcode.com/problems/arranging-coins)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/arranging-coins

class Solution {
 public:
  int arrangeCoins(int n) {
    int ret = 0, next = 0;
    while (n > next) n -= ++next, ++ret;
    return ret;
  }
};
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
