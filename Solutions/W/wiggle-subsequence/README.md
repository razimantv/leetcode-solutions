# Wiggle subsequence

[Problem link](https://leetcode.com/problems/wiggle-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/wiggle-subsequence

class Solution {
 public:
  int wiggleMaxLength(vector<int>& nums) {
    int N = nums.size(), up = (N > 0), down = up;

    for (int i = 1; i < N; ++i) {
      if (nums[i] > nums[i - 1])
        up = down + 1;
      else if (nums[i] < nums[i - 1])
        down = up + 1;
    }
    return max(up, down);
  }
};
```