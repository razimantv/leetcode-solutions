# Relocate marbles

[Problem link](https://leetcode.com/problems/relocate-marbles/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/relocate-marbles/

class Solution {
 public:
  vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom,
                              vector<int>& moveTo) {
    set<int> pos(nums.begin(), nums.end());
    for (int i = 0, n = moveFrom.size(); i < n; ++i) {
      pos.erase(moveFrom[i]);
      pos.insert(moveTo[i]);
    }
    return vector<int>(pos.begin(), pos.end());
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
