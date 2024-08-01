# Count subarrays with score less than k

[Problem link](https://leetcode.com/problems/count-subarrays-with-score-less-than-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k

class Solution {
 public:
  long long countSubarrays(vector<int>& nums, long long k) {
    int n = nums.size();
    long long pref[n + 1];
    pref[0] = 0;
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];

    long long ret = 0;
    for (int i = 0; i < n; ++i) {
      if ((pref[n] - pref[i]) * (n - i) < k) {
        ret += n - i;
        continue;
      }

      int start = i, end = n;
      while (end - start > 1) {
        int mid = (end + start) >> 1;
        ((pref[mid] - pref[i]) * (mid - i) < k ? start : end) = mid;
      }

      ret += start - i;
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
