# Minimum operations to reduce x to zero

[Problem link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

class Solution {
 public:
  int minOperations(vector<int>& nums, int x) {
    x = std::accumulate(nums.begin(), nums.end(), (int)0) - x;
    if (x < 0)
      return -1;
    else if (x == 0)
      return nums.size();
    int best = -1, n = nums.size();
    for (int i = 0, j = 0, cur = 0; j < n; ++j) {
      cur += nums[j];
      while (cur > x) cur -= nums[i++];
      if (cur == x) best = max(best, j - i + 1);
    }
    return best == -1 ? -1 : (n - best);
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
