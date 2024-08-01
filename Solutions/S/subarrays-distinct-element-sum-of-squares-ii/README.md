# Subarrays distinct element sum of squares ii

[Problem link](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

class Solution {
 public:
  int sumCounts(vector<int>& nums) {
    int n = nums.size(), base = 1;
    while (base < n) base <<= 1;
    vector<vector<long long>> seg(base << 1, vector<long long>(3));

    auto lazyfix = [&](int node, int L, int R) {
      auto& totsq = seg[node][0];
      auto& tot = seg[node][1];
      auto& lazy = seg[node][2];
      int cnt = R - L + 1;
      if (lazy) {
        if (node < base) {
          seg[node << 1][2] += lazy;
          seg[(node << 1) | 1][2] += lazy;
        }
        while (lazy) {
          totsq += 2 * tot + cnt;
          tot += cnt;
          lazy -= 1;
        }
      }
    };

    function<void(int, int, int, int, int)> update = [&](int node, int L, int R,
                                                         int l, int r) {
      // lazy: processing has not been done for this node

      if (l == L and r == R) seg[node][2] += 1;
      if (seg[node][2]) lazyfix(node, L, R);
      if (l == L and r == R) return;

      int M = (L + R) >> 1, lc = node << 1, rc = lc | 1;
      if (seg[lc][2]) lazyfix(lc, L, M);
      if (seg[rc][2]) lazyfix(rc, M + 1, R);

      if (r <= M)
        update(lc, L, M, l, r);
      else if (l > M)
        update(rc, M + 1, R, l, r);
      else {
        update(lc, L, M, l, M);
        update(rc, M + 1, R, M + 1, r);
      }

      seg[node][0] = seg[lc][0] + seg[rc][0];
      seg[node][1] = seg[lc][1] + seg[rc][1];
      seg[node][2] = 0;
    };

    unordered_map<int, int> last;
    long long ret = 0;
    for (int i = 0; i < n; i += 1) {
      int x = nums[i];
      int start = last.count(x) ? last[x] + 1 : 0;
      update(1, 0, base - 1, start, i);
      ret += seg[1][0];
      last[x] = i;
    }

    return ret % 1000000007;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree) > [Lazy propagation](/Collections/segment-tree.md#lazy-propagation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
