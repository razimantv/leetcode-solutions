# Target sum

[Problem link](https://leetcode.com/problems/target-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/target-sum

class Solution {
 public:
  typedef unordered_map<int, int> waymap;
  waymap ways(vector<int>& ar, int start, int end) {
    waymap ret{{0, 1}};
    for (int i = start; i < end; ++i) {
      waymap next;
      for (auto [k, v] : ret) next[k + ar[i]] += v, next[k - ar[i]] += v;
      ret = next;
    }
    return ret;
  }

  int findTargetSumWays(vector<int>& nums, int target) {
    int n = nums.size(), l = n / 2, ret = 0;
    auto m1 = ways(nums, 0, l);
    for (auto [k, v] : ways(nums, l, n)) ret += m1[target - k] * v;
    return ret;
  }
};
```