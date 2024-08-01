# 3sum

[Problem link](https://leetcode.com/problems/3sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/3sum

class Solution {
 public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int N = nums.size();
    vector<vector<int>> ret;
    for (int j = 0; j < N; ++j) {
      int i = 0;
      if (j > 1 and nums[j] == nums[j - 2]) continue;
      if (j > 0 and nums[j] == nums[j - 1]) i = j - 1;
      for (int k = N - 1; i < j and j < k;) {
        int cur = nums[i] + nums[j] + nums[k];
        if (cur == 0) {
          ret.push_back({nums[i], nums[j], nums[k]});
          do ++i;
          while (i < j and nums[i - 1] == nums[i]);
        } else if (cur < 0)
          ++i;
        else
          --k;
      }
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
