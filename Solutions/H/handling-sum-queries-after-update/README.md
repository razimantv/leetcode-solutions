# Handling sum queries after update

[Problem link](https://leetcode.com/problems/handling-sum-queries-after-update/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution {
 public:
  struct segnode {
    int val;
    bool flip;
  };

  void split(vector<segnode>& seg, int node, int L, int R) {
    if (!seg[node].flip) return;
    seg[node].flip = false;
    if (L == R) return;
    for (int nc : {(node << 1), (node << 1) | 1}) {
      seg[nc].flip = !seg[nc].flip;
      seg[nc].val = ((R - L + 1) >> 1) - seg[nc].val;
    }
  }
  void flip(vector<segnode>& seg, int node, int l, int r, int L, int R) {
    split(seg, node, L, R);
    if (L == l and R == r) {
      seg[node].val = R - L + 1 - seg[node].val;
      seg[node].flip = true;
      return;
    }
    int M = (L + R) >> 1;
    if (l > M)
      flip(seg, (node << 1) | 1, l, r, M + 1, R);
    else if (r <= M)
      flip(seg, (node << 1), l, r, L, M);
    else
      flip(seg, (node << 1), l, M, L, M),
          flip(seg, (node << 1) | 1, M + 1, r, M + 1, R);

    seg[node].val = seg[node << 1].val + seg[(node << 1) | 1].val;
  }
  vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2,
                                vector<vector<int>>& queries) {
    int n = nums1.size(), base = 1;
    while (base < n) base <<= 1;
    vector<segnode> seg(base << 1);
    for (int i = 0; i < n; ++i) seg[base + i].val = nums1[i];
    for (int i = base; --i;)
      seg[i].val = seg[i << 1].val + seg[(i << 1) | 1].val;

    long long sum = accumulate(nums2.begin(), nums2.end(), 0ll);
    vector<long long> ret;
    for (auto& q : queries) {
      if (q[0] == 1) {
        flip(seg, 1, q[1], q[2], 0, base - 1);
      } else if (q[0] == 2) {
        sum += q[1] * (long long)seg[1].val;
      } else {
        ret.push_back(sum);
      }
    }
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree) > [Lazy propagation](/Collections/segment-tree.md#lazy-propagation)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Composition of operations](/Collections/mathematics.md#composition-of-operations)
