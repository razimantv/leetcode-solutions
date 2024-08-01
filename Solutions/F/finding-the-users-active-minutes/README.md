# Finding the users active minutes

[Problem link](https://leetcode.com/problems/finding-the-users-active-minutes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/finding-the-users-active-minutes

class Solution {
 public:
  vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
    map<int, set<int>> unique;
    for (auto& v : logs) {
      unique[v[0]].insert(v[1]);
    }

    vector<int> ret(k);
    for (auto& [u, s] : unique) {
      int c = s.size();
      if (c <= k) ret[c - 1]++;
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
