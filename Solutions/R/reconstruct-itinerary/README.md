# Reconstruct itinerary

[Problem link](https://leetcode.com/problems/reconstruct-itinerary)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reconstruct-itinerary

class Solution {
 public:
  pair<bool, vector<string>> it(map<string, multiset<string>>& adj,
                                string start) {
    if (adj.empty()) return {true, {start}};
    if (adj.count(start) == 0 or adj[start].empty()) return {false, {}};

    multiset<string> cur = adj[start];
    for (auto next : cur) {
      adj[start].erase(adj[start].find(next));
      if (adj[start].empty()) adj.erase(start);
      auto ret = it(adj, next);
      if (ret.first) {
        ret.second.push_back(start);
        return ret;
      }
      adj[start].insert(next);
    }
    return {false, {}};
  }

  vector<string> findItinerary(vector<vector<string>>& tickets) {
    map<string, multiset<string>> adj;
    for (auto e : tickets) adj[e[0]].insert(e[1]);
    auto ret = it(adj, "JFK");
    reverse(ret.second.begin(), ret.second.end());
    return ret.second;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
