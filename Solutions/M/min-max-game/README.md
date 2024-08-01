# Min max game

[Problem link](https://leetcode.com/problems/min-max-game)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/min-max-game

class Solution {
 public:
  int minMaxGame(vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    vector<int> v(n >> 1);
    for (int i = 0; 2 * i < n; ++i)
      if (i & 1)
        v[i] = max(nums[2 * i], nums[2 * i + 1]);
      else
        v[i] = min(nums[2 * i], nums[2 * i + 1]);
    return minMaxGame(v);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
