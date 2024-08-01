# Jump game ii

[Problem link](https://leetcode.com/problems/jump-game-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game-ii

class Solution {
 public:
  int jump(vector<int>& nums) {
    int n = nums.size();
    nums[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
      int best = n;
      for (int j = i + 1; j < n and j <= i + nums[i]; ++j)
        best = min(best, nums[j]);
      nums[i] = best + 1;
    }
    return nums[0];
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
