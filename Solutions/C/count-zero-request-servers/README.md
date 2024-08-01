# Count zero request servers

[Problem link](https://leetcode.com/problems/count-zero-request-servers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
 public:
  vector<int> countServers(int ns, vector<vector<int>>& logs, int x,
                           vector<int>& queries) {
    int n = logs.size(), q = queries.size();
    vector<int> idx(n + q);
    iota(idx.begin(), idx.end(), 0);
    auto time = [&](int i) { return (i < n) ? logs[i][1] : queries[i - n]; };
    sort(idx.begin(), idx.end(), [&](int i, int j) {
      int ti = time(i), tj = time(j);
      return (ti == tj) ? (i < j) : (ti < tj);
    });

    int good{};
    unordered_map<int, int> last;
    set<pair<int, int>> toremove;
    for (int index : idx) {
      int t = time(index);
      while (!toremove.empty() and toremove.begin()->first < t - x) {
        auto [tt, ii] = *toremove.begin();
        toremove.erase(toremove.begin());
        --good;
        last.erase(ii);
      }
      if (index < n) {
        int server = logs[index][0];
        if (last.count(server)) {
          toremove.erase({last[server], server});
          --good;
        }
        toremove.insert({last[server] = t, server});
        ++good;
      } else {
        queries[index - n] = ns - good;
      }
    }
    return queries;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Queries and updates together](/Collections/sorting.md#queries-and-updates-together)
* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
