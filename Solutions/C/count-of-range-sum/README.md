# Count of range sum

[Problem link](https://leetcode.com/problems/count-of-range-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-of-range-sum

class Solution {
 public:
  vector<int> seg;
  int base;

  void insert(int pos) {
    for (pos += base; pos; pos >>= 1) ++seg[pos];
  }

  int query(int pos) {
    if (pos < 0) return 0;
    int ret = seg[pos += base];
    for (; pos > 1; pos >>= 1)
      if (pos & 1) ret += seg[pos ^ 1];
    return ret;
  }

  int countRangeSum(vector<int>& nums, int lower, int upper) {
    int N = nums.size();
    long long tot = 0;
    set<long long> s{tot};
    for (int i = 0; i < N; ++i) s.insert(tot += nums[i]);

    map<long long, int> cc;
    cc[LONG_LONG_MIN] = -1;
    int L = 0;
    for (long long n : s) cc[n] = L++;

    base = 1;
    while (base < L) base <<= 1;
    seg.resize(base << 1);
    insert(cc[0]);

    tot = 0;
    int ret = 0;
    for (int n : nums) {
      tot += n;
      auto mit = cc.upper_bound(tot - lower);
      ret += query((--mit)->second);
      mit = cc.lower_bound(tot - upper);
      ret -= query((--mit)->second);
      insert(cc[tot]);
    }
    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
