# Smallest even multiple

[Problem link](https://leetcode.com/problems/smallest-even-multiple/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-even-multiple/

class Solution {
 public:
  int smallestEvenMultiple(int n) { return (n & 1) ? (n * 2) : n; }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
