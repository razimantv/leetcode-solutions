# Make array empty

[Problem link](https://leetcode.com/problems/make-array-empty/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-array-empty/

class Solution {
 public:
  long long countOperationsToEmptyArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(),
         [&](int i, int j) { return nums[i] < nums[j]; });
    long long ret = n + idx[0];

    int base = 1;
    while (base < n) base <<= 1;
    vector<int> seg(base << 1);
    fill(seg.begin() + base, seg.begin() + base + n, 1);
    for (int i = base; --i;) seg[i] = seg[i << 1] + seg[(i << 1) | 1];

    auto sum = [&](int x) {
      if (x < 0) return 0;

      int node = x + base, ret = seg[node];
      while (node > 1) {
        if (node & 1) ret += seg[node ^ 1];
        node >>= 1;
      }
      return ret;
    };

    auto decrement = [&](int x) {
      int node = x + base;
      while (node) {
        --seg[node];
        node >>= 1;
      }
    };

    for (int i = 1; i < n; ++i) {
      int prev = idx[i - 1], cur = idx[i];
      decrement(prev);
      // prev < cur: sum(prev..cur-1)
      // else: sum(0..n-1) - sum(cur..prev)

      int rotations = (prev < cur) ? (sum(cur - 1) - sum(prev))
                                   : (seg[1] - sum(prev) + sum(cur - 1));
      ret += rotations;
    }
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
