# Find the pivot integer

[Problem link](https://leetcode.com/problems/find-the-pivot-integer/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
 public:
  int pivotInteger(int n) {
    int a = n * (n + 1) / 2;
    for (int i = 1; i <= n; ++i)
      if (i * (i + 1) / 2 == a - i * (i - 1) / 2) return i;
    return -1;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Closed form expressions](/README.md#Mathematics-Closed_form_expressions)
* [Simple implementation](/README.md#Simple_implementation)
