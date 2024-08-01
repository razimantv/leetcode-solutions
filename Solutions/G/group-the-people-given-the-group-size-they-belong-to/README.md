# Group the people given the group size they belong to

[Problem link](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
public:
  vector<vector<int>> groupThePeople(vector<int> &sizes) {
    unordered_map<int, vector<int>> groups;
    vector<vector<int>> ret;
    for (int i = 0, n = sizes.size(); i < n; ++i) {
      int g = sizes[i];
      auto &group = groups[g];
      group.push_back(i);
      if (group.size() == g) {
        ret.push_back(group);
        group.clear();
      }
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
