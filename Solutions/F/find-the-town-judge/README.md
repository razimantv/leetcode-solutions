# Find the town judge

[Problem link](https://leetcode.com/problems/find-the-town-judge)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-town-judge

class Solution {
 public:
  int findJudge(int N, vector<vector<int>>& trust) {
    vector<int> degree(N + 1, 0);

    for (auto elem : trust) {
      degree[elem[0]]--;
      degree[elem[1]]++;
    }

    for (int i = 1; i <= N; ++i) {
      if (degree[i] == N - 1) return i;
    }
    return -1;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
