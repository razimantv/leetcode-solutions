# Merge similar items

[Problem link](https://leetcode.com/problems/merge-similar-items)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-similar-items

class Solution {
 public:
  vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1,
                                        vector<vector<int>>& items2) {
    map<int, int> m;
    for (auto& v : items1) m[v[0]] += v[1];
    for (auto& v : items2) m[v[0]] += v[1];

    vector<vector<int>> ret;
    for (auto [k, v] : m) ret.push_back({k, v});
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
