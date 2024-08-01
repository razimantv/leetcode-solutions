# Count total number of colored cells

[Problem link](https://leetcode.com/problems/count-total-number-of-colored-cells/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution {
 public:
  long long coloredCells(int n) {
    return n * (long long)n + (n - 1) * (long long)(n - 1);
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
