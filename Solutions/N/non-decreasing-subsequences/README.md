# Non decreasing subsequences

[Problem link](https://leetcode.com/problems/non-decreasing-subsequences/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/non-decreasing-subsequences/

class Solution {
 public:
  vector<vector<int>> findSubsequences(vector<int>& nums) {
    int n = nums.size();
    set<vector<int>> s;
    for (int mask = 1; mask < (1 << n); ++mask) {
      if (!(mask & (mask - 1))) continue;
      vector<int> cur;
      for (int i = 0; i < n; ++i) {
        if (!(mask & (1 << i))) continue;
        if (!cur.empty() and cur.back() > nums[i]) {
          cur.clear();
          break;
        }
        cur.push_back(nums[i]);
      }
      if (!cur.empty()) s.insert(cur);
    }
    vector<vector<int>> ret;
    for (const auto& v : s) ret.push_back(v);
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
