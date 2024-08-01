# Minimum genetic mutation

[Problem link](https://leetcode.com/problems/minimum-genetic-mutation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-genetic-mutation

class Solution {
 public:
  int minMutation(string start, string end, vector<string>& bank) {
    unordered_set<string> good;
    for (const string& s : bank) good.insert(s);
    if (good.count(start)) good.erase(start);

    queue<pair<string, int>> bfsq;
    bfsq.push({start, 0});
    while (!bfsq.empty()) {
      auto [cur, depth] = bfsq.front();
      bfsq.pop();

      for (int i = 0; i < 8; ++i) {
        char c = cur[i];
        for (char x : "ACGT") {
          cur[i] = x;
          if (good.count(cur)) {
            if (cur == end) return depth + 1;
            bfsq.push({cur, depth + 1});
            good.erase(cur);
          }
        }
        cur[i] = c;
      }
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
