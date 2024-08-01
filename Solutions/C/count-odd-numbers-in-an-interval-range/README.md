# Count odd numbers in an interval range

[Problem link](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution {
 public:
  int f(int x) { return x - x / 2; }
  int countOdds(int low, int high) { return f(high) - f(low - (low > 0)); }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
