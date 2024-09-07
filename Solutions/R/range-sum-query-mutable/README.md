# Range sum query mutable

[Problem link](https://leetcode.com/problems/range-sum-query-mutable)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-sum-query-mutable

class NumArray {
 public:
  vector<int> seg;
  int base;
  NumArray(vector<int>& nums) {
    int n = nums.size();
    base = 1;
    while (base < n) base <<= 1;
    seg.resize(base << 1);
    for (int i = 0; i < n; ++i) seg[base + i] = nums[i];
    for (int i = base - 1; i; --i) seg[i] = seg[i << 1] + seg[(i << 1) | 1];
  }

  void update(int index, int val) {
    val -= seg[index += base];
    while (index) seg[index] += val, index >>= 1;
  }

  int sumRange(int left, int right) {
    if (left > 0) return sumRange(0, right) - sumRange(0, left - 1);
    int ret = seg[right += base];
    while (right > 1) {
      if (right & 1) ret += seg[right ^ 1];
      right >>= 1;
    }
    return ret;
  }
};

```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
