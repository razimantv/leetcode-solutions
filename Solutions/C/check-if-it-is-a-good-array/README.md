# Check if it is a good array

[Problem link](https://leetcode.com/problems/check-if-it-is-a-good-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-it-is-a-good-array

class Solution {
 public:
  bool isGoodArray(vector<int>& nums) {
    int g = 0;
    for (int n : nums)
      if ((g = __gcd(g, n)) == 1) return true;
    return false;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
