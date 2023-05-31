# Arithmetic slices ii subsequence

[Problem link](https://leetcode.com/problems/arithmetic-slices-ii-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence

class Solution {
 public:
  int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    vector<unordered_map<long long, int>> mvec(n);

    int ret = -(n * (n - 1)) / 2;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        long long diff = nums[i] - (long long)nums[j];
        ++mvec[i][diff];
        ++ret;
        if (mvec[j].count(diff))
          mvec[i][diff] += mvec[j][diff], ret += mvec[j][diff];
      }
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
