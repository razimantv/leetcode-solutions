# Delivering boxes from storage to ports

[Problem link](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports

class Solution {
 public:
  // DP[i] = min_{valid j<i} (DP[j] - sumchanges[j+1]) + 2 + sumchanges[i]

  vector<int> seg;
  int base;

  void insert(int pos, int val) {
    seg[pos += base] = val;
    for (pos >>= 1; pos; pos >>= 1)
      seg[pos] = min(seg[pos << 1], seg[(pos << 1) | 1]);
  }

  int query(int n, int l, int r, int L, int R) {
    if (l == L and r == R) return seg[n];

    int M = (L + R) >> 1;
    if (l >= M)
      return query((n << 1) | 1, l, r, M, R);
    else if (r <= M)
      return query((n << 1), l, r, L, M);
    else
      return min(query((n << 1), l, M, L, M), query((n << 1) | 1, M, r, M, R));
  }

  int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes,
                    int maxWeight) {
    int N = boxes.size();

    vector<long long> wsum(N + 1);
    for (int i = 0; i < N; ++i) wsum[i + 1] = wsum[i] + boxes[i][1];

    base = 1;
    while (base <= N) base <<= 1;
    seg.resize(base << 1);
    insert(0, 0);

    int chg = 0;
    for (int i = 0; i < N; ++i) {
      int p = lower_bound(wsum.begin(), wsum.end(), wsum[i + 1] - maxWeight) -
              wsum.begin();
      int L = min(i + 1 - p, maxBoxes);
      int dp = query(1, max(0, i + 1 - L), i + 1, 0, base) + chg;
      if (i < N - 1 and boxes[i][0] != boxes[i + 1][0]) ++chg;
      insert(i + 1, dp + 2 - chg);
    }
    return seg[base + N] + chg;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Binary search](/Collections/binary-search.md#binary-search) > [Prefix sum](/Collections/binary-search.md#prefix-sum)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Segment tree](/Collections/dynamic-programming.md#segment-tree)
