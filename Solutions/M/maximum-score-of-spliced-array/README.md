# Maximum score of spliced array

[Problem link](https://leetcode.com/problems/maximum-score-of-spliced-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-score-of-spliced-array

class Solution {
 public:
  int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), tot1 = accumulate(nums1.begin(), nums1.end(), 0),
        tot2 = accumulate(nums2.begin(), nums2.end(), 0);

    for (int i = 0; i < n; ++i) nums2[i] -= nums1[i];
    int bestp = 0, bestm = 0;
    for (int i = 0, cur = 0, prevbestp = 0, prevbestm = 0; i < n; ++i) {
      bestp = max(bestp, (cur += nums2[i]) - prevbestp);
      bestm = max(bestm, -cur - prevbestm);
      prevbestp = min(prevbestp, cur);
      prevbestm = min(prevbestm, -cur);
    }
    return max(tot1 + bestp, tot2 + bestm);
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
