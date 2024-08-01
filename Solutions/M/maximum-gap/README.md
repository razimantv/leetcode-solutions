# Maximum gap

[Problem link](https://leetcode.com/problems/maximum-gap)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-gap

class Solution {
 public:
  int maximumGap(vector<int>& nums) {
    int N = nums.size();
    if (N == 1) return 0;
    sort(nums.begin(), nums.end());
    int best = 0;
    for (int i = 1; i < N; ++i) best = max(best, nums[i] - nums[i - 1]);
    return best;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
