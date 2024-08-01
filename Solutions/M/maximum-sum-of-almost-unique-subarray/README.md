# Maximum sum of almost unique subarray

[Problem link](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution {
 public:
  long long maxSum(vector<int>& nums, int m, int k) {
    unordered_map<int, int> cnt;
    long long tot{}, best{};
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (i >= k) {
        if (!--cnt[nums[i - k]]) cnt.erase(nums[i - k]);
        tot -= nums[i - k];
      }
      tot += nums[i];
      ++cnt[nums[i]];
      if (cnt.size() >= m) best = max(best, tot);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
