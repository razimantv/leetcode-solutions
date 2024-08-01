# Convert an array into a 2d array with conditions

[Problem link](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution {
 public:
  vector<vector<int>> findMatrix(vector<int>& nums) {
    unordered_map<int, int> cnt;
    for (int x : nums) ++cnt[x];
    vector<vector<int>> ret;
    for (auto [k, v] : cnt) {
      for (int i = 0; i < v; ++i) {
        if (i == ret.size()) ret.push_back({});
        ret[i].push_back(k);
      }
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
