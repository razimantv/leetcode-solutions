# Minimum interval to include each query

[Problem link](https://leetcode.com/problems/minimum-interval-to-include-each-query)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-interval-to-include-each-query

class Solution {
 public:
  vector<int> minInterval(vector<vector<int>>& intervals,
                          vector<int>& queries) {
    vector<tuple<int, int, int, int>> event;
    for (int i = 0, n = intervals.size(); i < n; ++i) {
      auto& v = intervals[i];
      event.push_back({v[0], 0, v[1] - v[0] + 1, i});
      event.push_back({v[1], 2, v[1] - v[0] + 1, i});
    }

    int Q = queries.size();
    for (int i = 0; i < Q; ++i) event.push_back({queries[i], 1, 0, i});
    sort(event.begin(), event.end());

    vector<int> ret(Q);
    set<pair<int, int>> cur;
    for (auto [t, type, l, id] : event) {
      if (type == 0)
        cur.insert({l, id});
      else if (type == 2)
        cur.erase({l, id});
      else if (cur.empty())
        ret[id] = -1;
      else
        ret[id] = cur.begin()->first;
    }
    return ret;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Endpoint sorting](/Collections/intervals.md#endpoint-sorting)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
