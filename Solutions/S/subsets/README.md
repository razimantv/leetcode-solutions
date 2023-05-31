# Subsets

[Problem link](https://leetcode.com/problems/subsets)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subsets

class Solution {
 public:
  vector<vector<int>> subsets(vector<int>& nums) {
    int N = nums.size();
    vector<vector<int>> ret(1 << N);
    for (int i = 0, base = 1; i < N; ++i, base <<= 1) {
      for (int j = 0; j < base; ++j) {
        ret[base | j] = ret[j];
        ret[j].push_back(nums[i]);
      }
    }
    return ret;
  }
};
```