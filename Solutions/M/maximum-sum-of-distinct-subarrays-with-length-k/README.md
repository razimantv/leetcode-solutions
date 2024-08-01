# Maximum sum of distinct subarrays with length k

[Problem link](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution {
 public:
  long long maximumSubarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    unordered_map<int, int> cnt;
    long long cur{}, best{};
    for (int i = 0, j = 0; j < n; ++j) {
      while (cnt[nums[j]] or j - i >= k) {
        cur -= nums[i];
        --cnt[nums[i++]];
      }

      cur += nums[j];
      ++cnt[nums[j]];
      if (j - i + 1 == k) {
        best = max(best, cur);
      }
    }
    return best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
