# Minimum operations to make array equal

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-array-equal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution {
 public:
  int minOperations(int n) { return (n - n / 2) * (n / 2); }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Closed form expressions](/README.md#Mathematics-Closed_form_expressions)
