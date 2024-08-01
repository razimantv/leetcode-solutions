# Jump game

[Problem link](https://leetcode.com/problems/jump-game)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game

class Solution {
 public:
  bool canJump(vector<int>& nums) {
    int N = nums.size();
    int lim = nums[0];
    if (lim >= N - 1) return true;
    for (int i = 1; i <= lim; ++i) {
      if ((lim = max(lim, i + nums[i])) >= N - 1) return true;
    }
    return false;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
