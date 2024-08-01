# Count pairs with xor in a range

[Problem link](https://leetcode.com/problems/count-pairs-with-xor-in-a-range)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range

class Solution {
 public:
  vector<int> seg;
  int get(int node, int low, int high, int n, int mask) {
    if (low <= 0 and high >= mask - 1)
      return seg[node];
    else if (high < 0 or low >= mask)
      return 0;
    mask >>= 1;
    int bit = n & mask, invbit = mask ^ bit, ret = 0;
    ret += get(node * 2, low - bit, high - bit, n, mask);
    ret += get(node * 2 + 1, low - invbit, high - invbit, n, mask);
    return ret;
  }
  int countPairs(vector<int>& nums, int low, int high) {
    int ret = 0, lim = 32768;
    seg.resize(2 * lim);
    for (int n : nums) {
      ret += get(1, low, high, n, lim);
      for (int pos = lim + n; pos; pos >>= 1) seg[pos]++;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Segment tree](/Collections/segment-tree.md#segment-tree)
