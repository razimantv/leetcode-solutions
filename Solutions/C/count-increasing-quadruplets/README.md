# Count increasing quadruplets

[Problem link](https://leetcode.com/problems/count-increasing-quadruplets/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
 public:
  long long countQuadruplets(vector<int>& nums) {
    int n = nums.size(), base = 1;
    while (base <= n) base <<= 1;
    vector<vector<long long>> seg(3, vector<long long>(base << 1));
    long long ret{};
    for (int x : nums) {
      long long cur = 1;
      for (int i = 0; i < 3; ++i) {
        long long next{};
        for (int node = base + x; node; node >>= 1) {
          seg[i][node] += cur;
          if (node & 1) next += seg[i][node ^ 1];
        }
        cur = next;
      }
      ret -= cur;
    }

    for (int i = 0; i < n; ++i) {
      vector<int> seg2(base << 1);

      for (int j = i + 1; j < n; ++j) {
        int x = nums[j];
        if (x < nums[i]) continue;
        long long cnt{};
        for (int node = base + x; node; node >>= 1) {
          ++seg2[node];
          if (node & 1) cnt += seg2[node ^ 1];
        }
        ret += cnt * (cnt - 1) / 2;
      }
    }

    return ret;
  }
};
```
## Tags

* [Segment tree](/Collections/segment-tree.md#segment-tree)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Segment tree](/Collections/dynamic-programming.md#segment-tree)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
