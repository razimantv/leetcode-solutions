# Custom sort string

[Problem link](https://leetcode.com/problems/custom-sort-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/custom-sort-string

class Solution {
 public:
  string customSortString(string order, string str) {
    vector<int> cnt(26, 26);
    for (int i = 0, n = order.size(); i < n; ++i) cnt[order[i] - 'a'] = i;
    sort(str.begin(), str.end(),
         [&](char a, char b) { return cnt[a - 'a'] < cnt[b - 'a']; });
    return str;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
