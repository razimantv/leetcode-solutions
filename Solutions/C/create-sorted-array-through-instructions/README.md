# Create sorted array through instructions

[Problem link](https://leetcode.com/problems/create-sorted-array-through-instructions)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/create-sorted-array-through-instructions

class Solution {
 public:
  static const int base = 1 << 17, mod = 1'000'000'007;
  int seg[base << 1];

  int createSortedArray(vector<int>& ar) {
    int ret = 0;
    for (int i = 0, n = ar.size(); i < n; ++i) {
      int left = 0;
      for (int cur = base + ar[i]; cur; cur >>= 1) {
        if (cur & 1) left += seg[cur ^ 1];
        seg[cur]++;
      }
      ret += min(left, i + 1 - left - seg[base + ar[i]]);
      if (ret >= mod) ret -= mod;
    }
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
