# Factorial trailing zeroes

[Problem link](https://leetcode.com/problems/factorial-trailing-zeroes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution {
 public:
  int trailingZeroes(int n) {
    int ret = 0;
    while (n /= 5) ret += n;
    return ret;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
