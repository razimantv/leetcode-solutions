# Frequency of the most frequent element

[Problem link](https://leetcode.com/problems/frequency-of-the-most-frequent-element)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/frequency-of-the-most-frequent-element

class Solution {
 public:
  int maxFrequency(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int n = nums.size();

    int best = 0;
    for (int i = n - 1, j = n - 1, cur = 0; i >= 0; --i) {
      while (cur <= k and j >= 0) {
        if (j >= 0) --j;
        if (j >= 0) cur += nums[i] - nums[j];
      }
      best = max(best, i - j);
      if (i) cur -= (i - j) * (nums[i] - nums[i - 1]);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
