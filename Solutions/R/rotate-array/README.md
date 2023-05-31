# Rotate array

[Problem link](https://leetcode.com/problems/rotate-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rotate-array

class Solution {
 public:
  void rotate(vector<int>& nums, int k) {
    int N = nums.size();
    k %= N;
    if (k == 0) return;
    k = N - k;
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
    reverse(nums.begin(), nums.end());
  }
};
```