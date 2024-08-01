# Closest room

[Problem link](https://leetcode.com/problems/closest-room)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/closest-room

class Solution {
 public:
  vector<int> closestRoom(vector<vector<int>>& rooms,
                          vector<vector<int>>& queries) {
    int q = queries.size();
    for (int i = 0; i < q; ++i) queries[i] = {queries[i][1], queries[i][0], i};
    sort(queries.begin(), queries.end(), greater<vector<int>>());

    int n = rooms.size();
    for (auto& r : rooms) swap(r[0], r[1]);
    sort(rooms.begin(), rooms.end(), greater<vector<int>>());

    set<int> cur;
    vector<int> ret(q);
    for (int i = 0, j = 0; i < q; ++i) {
      while (j < n and rooms[j][0] >= queries[i][0]) cur.insert(rooms[j++][1]);
      if (cur.empty()) {
        ret[queries[i][2]] = -1;
        continue;
      }
      auto sit = cur.lower_bound(queries[i][1]);
      if (sit == cur.end())
        ret[queries[i][2]] = *--sit;
      else {
        int x = *sit;
        if (sit != cur.begin()) {
          int y = *--sit;
          if (queries[i][1] - y <= x - queries[i][1]) x = y;
        }
        ret[queries[i][2]] = x;
      }
    }

    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
