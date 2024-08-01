# Keys and rooms

[Problem link](https://leetcode.com/problems/keys-and-rooms)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/keys-and-rooms

class Solution {
 public:
  bool canVisitAllRooms(vector<vector<int>>& rooms) {
    int N = rooms.size(), cnt = 1;
    vector<char> seen(N);

    vector<int> toprocess{0};
    seen[0] = 1;
    while (!toprocess.empty()) {
      int u = toprocess.back();
      toprocess.pop_back();
      for (int v : rooms[u])
        if (!seen[v]) seen[v] = 1, ++cnt, toprocess.push_back(v);
    }
    return cnt == N;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
