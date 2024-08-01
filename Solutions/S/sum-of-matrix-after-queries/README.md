# Sum of matrix after queries

[Problem link](https://leetcode.com/problems/sum-of-matrix-after-queries/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
 public:
  long long matrixSumQueries(int n, vector<vector<int>>& queries) {
    long long ret{};
    unordered_set<int> rowseen, colseen;
    for (int i = queries.size() - 1; i >= 0; --i) {
      const auto& query = queries[i];
      int type = query[0], index = query[1], val = query[2];
      if (type == 0 and !rowseen.count(index)) {
        ret += (n - colseen.size()) * 1ll * val;
        rowseen.insert(index);
      } else if (type == 1 and !colseen.count(index)) {
        ret += (n - rowseen.size()) * 1ll * val;
        colseen.insert(index);
      }
    }
    return ret;
  }
};
```
## Tags

* [Time reversed simulation](/Collections/time-reversed-simulation.md#time-reversed-simulation)
* [Hashmap](/Collections/hashmap.md#hashmap)
