# Minimum moves to equal array elements ii

[Problem link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution {
 public:
  int minMoves2(vector<int>& nums) {
    int N = nums.size(), M = N >> 1;
    nth_element(nums.begin(), nums.begin() + M, nums.end());

    int best = 0;
    for (int i = 0; i < M; ++i) best += nums[M] - nums[i];
    for (int i = M + 1; i < N; ++i) best += nums[i] - nums[M];
    return best;
  }
};
```
## Tags

* [Quick Select](/Collections/quick-select.md#quick-select)
