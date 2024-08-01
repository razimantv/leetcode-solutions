# Number of pairs satisfying inequality

[Problem link](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
 public:
  long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int diff) {
    int n = nums1.size(), m = 1e5, M = -1e5;
    for (int i = 0; i < n; ++i) {
      nums1[i] -= nums2[i];
      m = min(m, nums1[i]);
      M = max(M, nums1[i]);
    }

    int offset = -min(m, m + diff);
    int maxl = offset + max(M, M + diff + 1);
    int base = 1;
    while (base <= maxl) base <<= 1;

    vector<int> seg(base << 1);
    long long ret = 0;
    for (int i = 0; i < n; ++i) {
      int x = nums1[i] + offset + base;
      for (int node = x + diff + 1; node > 1; node >>= 1)
        if (node & 1) ret += seg[node ^ 1];
      for (int node = x; node; node >>= 1) seg[node]++;
    }
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Expression rearrangement](/Collections/mathematics.md#expression-rearrangement)
