# Minimum cost to make all characters equal

[Problem link](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
 public:
  long long minimumCost(string s) {
    vector<int> chunks{0};
    for (int i = 0, cur = 0; s[i]; ++i) {
      if (i and s[i] != s[i - 1]) chunks.push_back(0);
      ++chunks.back();
    }

    int n = chunks.size();
    vector<long long> left(n), right(n);
    for (auto [i, pref] = make_pair(0, 0ll); i < n; ++i) {
      left[i] = pref + (i ? left[i - 1] : 0);
      pref += chunks[i];
    }

    long long ret = LONG_LONG_MAX;
    for (auto [i, pref] = make_pair(n - 1, 0ll); i >= 0; --i) {
      right[i] = pref + (i < n - 1 ? right[i + 1] : 0);
      pref += chunks[i];
      ret = min(ret, left[i] + right[i]);
    }
    return ret;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
