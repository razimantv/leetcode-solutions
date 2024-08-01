# Maximum subarray

[Problem link](https://leetcode.com/problems/maximum-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-subarray

class Solution {
 public:
  int maxSubArray(vector<int>& nums) {
    int best = nums[0], minprefix = 0, cum = 0;
    for (int n : nums) {
      cum += n;
      best = std::max(best, cum - minprefix);
      minprefix = std::min(cum, minprefix);
    }
    return best;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
