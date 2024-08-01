# Longest increasing subsequence ii

[Problem link](https://leetcode.com/problems/longest-increasing-subsequence-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

class Solution {
 public:
  vector<int> seg;
  static const int base = 1 << 17;

  int query(int node, int L, int R, int l, int r) {
    if (l == L and r == R) return seg[node];
    int M = (L + R) >> 1, lc = node << 1, rc = lc | 1;
    if (r <= M)
      return query(lc, L, M, l, r);
    else if (l > M)
      return query(rc, M + 1, R, l, r);
    else
      return max(query(lc, L, M, l, M), query(rc, M + 1, R, M + 1, r));
  }
  int lengthOfLIS(vector<int>& nums, int k) {
    int n = nums.size(), best = 0;
    seg = vector<int>(base * 2);

    for (int x : nums) {
      int start = max(0, x - k), end = x - 1;
      int cur = 1 + query(1, 0, base - 1, start, end);
      best = max(best, cur);
      for (int node = base | x; node; node >>= 1)
        seg[node] = max(seg[node], cur);
    }
    return best;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
