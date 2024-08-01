# Check array formation through concatenation

[Problem link](https://leetcode.com/problems/check-array-formation-through-concatenation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-array-formation-through-concatenation

class Solution {
 public:
  bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
    unordered_map<int, int> x;
    for (int i = 0, n = pieces.size(); i < n; ++i) x[pieces[i][0]] = i;
    for (int i = 0, n = arr.size(); i < n;) {
      if (!x.count(arr[i])) return false;
      auto& p = pieces[x[arr[i]]];
      if (i + p.size() > n) return false;
      for (int j = 0, m = p.size(); j < m; ++i, ++j)
        if (arr[i] != p[j]) return false;
    }
    return true;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
