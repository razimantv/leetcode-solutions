# Minimum sum of squared difference

[Problem link](https://leetcode.com/problems/minimum-sum-of-squared-difference)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-sum-of-squared-difference

class Solution {
 public:
  int maxequal(vector<int>& ar, int k) {
    long long tot = 0;
    int n = ar.size();
    for (int i = 0; i < n; ++i) {
      tot += ar[i];
      if (tot - ar[i] * (long long)(i + 1) > k) return i - 1;
    }
    return n - 1;
  }

  long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1,
                             int k2) {
    int n = nums1.size();
    for (int i = 0; i < n; ++i) nums1[i] = abs(nums1[i] - nums2[i]);
    sort(nums1.begin(), nums1.end(), greater<int>());

    int k = k1 + k2;
    if (accumulate(nums1.begin(), nums1.end(), 0ll) <= k) return 0;

    int l = maxequal(nums1, k);
    for (int i = 0; i <= l; ++i) {
      k -= nums1[i] - nums1[l];
      nums1[i] = nums1[l];
    }
    for (int i = 0; i <= l; ++i) {
      nums1[i] -= k / (l + 1);
    }
    k %= l + 1;
    for (int i = 0; k; --k, ++i) --nums1[i];

    long long ret = 0;
    for (int x : nums1) ret += x * (long long)x;
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
