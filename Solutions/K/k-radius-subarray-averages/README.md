# K radius subarray averages

[Problem link](https://leetcode.com/problems/k-radius-subarray-averages/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/k-radius-subarray-averages/

class Solution {
 public:
  vector<int> getAverages(vector<int>& nums, int k) {
    int n = nums.size(), w = 2 * k + 1;

    vector<int> ret(n, -1);
    if (n < w) return ret;
    long long tot = accumulate(nums.begin(), nums.begin() + 2 * k + 1, 0ll);
    ret[k] = tot / w;
    for (int l = 0, m = k + 1, r = 2 * k + 1; r < n; ++l, ++m, ++r) {
      tot += nums[r] - nums[l];
      ret[m] = tot / w;
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
