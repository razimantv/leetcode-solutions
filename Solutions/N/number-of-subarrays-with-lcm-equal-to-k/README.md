# Number of subarrays with lcm equal to k

[Problem link](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution {
 public:
  int subarrayLCM(vector<int>& nums, int k) {
    int n = nums.size(), ret{};
    for (int i = 0; i < n; ++i) {
      for (int j = i, l = 1; j < n; ++j) {
        l = (l * nums[j]) / __gcd(l, nums[j]);
        if (l == k)
          ++ret;
        else if (l > k)
          break;
      }
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
