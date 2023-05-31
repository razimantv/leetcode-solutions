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

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
* [Array scanning](/README.md#Array_scanning) > [From both ends of array](/README.md#Array_scanning-From_both_ends_of_array)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Dynamic programming](/README.md#Dynamic_programming)
