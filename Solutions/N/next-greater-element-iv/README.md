# Next greater element iv

[Problem link](https://leetcode.com/problems/next-greater-element-iv/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/next-greater-element-iv/

class Solution {
 public:
  vector<int> secondGreaterElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int a, int b) {
      if (nums[a] != nums[b]) return nums[a] > nums[b];
      return a < b;
    });

    int base = 1;
    while (base < n) base <<= 1;
    vector<int> seg(base << 1);

    vector<int> ret(n);
    for (int x : idx) {
      int cur = 1;
      for (int node = base + x; node; node >>= 1) {
        ++seg[node];
        if (node & 1) cur += seg[node ^ 1];
      }

      cur += 2;
      if (seg[1] < cur) {
        ret[x] = -1;
        continue;
      }

      for (int node = 1;;) {
        if (node >= base) {
          ret[x] = nums[node - base];
          break;
        }
        if (seg[node << 1] >= cur)
          node <<= 1;
        else
          cur -= seg[node << 1], node = (node << 1) | 1;
      }
    }

    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
