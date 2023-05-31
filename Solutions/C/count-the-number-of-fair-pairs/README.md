# Count the number of fair pairs

[Problem link](https://leetcode.com/problems/count-the-number-of-fair-pairs/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution {
 public:
  long long countFairPairs(vector<int>& nums, int lower, int upper) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    long long ret{};
    for (int i = n - 1, x = 0, y = 0; i >= 0; --i) {
      while (x < n and nums[i] + nums[x] < lower) ++x;
      while (y < n and nums[i] + nums[y] <= upper) ++y;
      ret += y - x;
      if (2 * nums[i] >= lower and 2 * nums[i] <= upper) --ret;
    }
    return ret / 2;
  }
};
```
## Tags

* [Sorting](/README.md#Sorting)
* [Sliding window](/README.md#Sliding_window)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
