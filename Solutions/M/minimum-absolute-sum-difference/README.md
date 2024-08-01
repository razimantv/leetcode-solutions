# Minimum absolute sum difference

[Problem link](https://leetcode.com/problems/minimum-absolute-sum-difference)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-absolute-sum-difference

class Solution {
 public:
  int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
    int N = nums1.size();
    set<int> s;

    long long tot = 0, best = 0;
    int MOD = 1'000'000'007;
    for (int i = 0; i < N; ++i) {
      tot += abs(nums1[i] - nums2[i]);
      s.insert(nums1[i]);
    }

    best = tot;
    for (int i = 0; i < N; ++i) {
      auto sit = s.lower_bound(nums2[i]);
      int curbest = abs(nums2[i] - nums1[i]), cp = curbest;
      if (sit != s.end()) curbest = min(curbest, abs(nums2[i] - *sit));
      if (sit != s.begin()) {
        --sit;
        curbest = min(curbest, abs(nums2[i] - *sit));
      }
      best = min(best, tot + curbest - cp);
    }
    return best % MOD;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
