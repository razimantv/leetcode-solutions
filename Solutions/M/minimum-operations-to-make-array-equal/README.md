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

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
