# Find the shortest superstring

[Problem link](https://leetcode.com/problems/find-the-shortest-superstring)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-shortest-superstring

class Solution {
 public:
  string shortestSuperstring(vector<string>& words) {
    int N = words.size();
    vector<int> L(N);
    for (int i = 0; i < N; ++i) L[i] = words[i].size();

    vector<vector<int>> common(N, vector<int>(N));
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j) {
        if (i == j) continue;
        int Lmax = min(L[i], L[j]);
        for (int l = 1; l <= Lmax; ++l) {
          if (words[i].substr(L[i] - l) == words[j].substr(0, l))
            common[i][j] = l;
        }
      }

    vector<vector<string>> DP(1 << N, vector<string>(N));
    for (int i = 0; i < N; ++i) DP[1 << i][i] = words[i];
    for (int mask = 1; mask < (1 << N); ++mask) {
      if (!(mask & (mask - 1))) continue;
      for (int i = 0; i < N; ++i) {
        if (!(mask & (1 << i))) continue;
        int newmask = mask ^ (1 << i);
        for (int j = 0; j < N; ++j) {
          if (j != i and (newmask & (1 << j))) {
            string cur = DP[newmask][j] + words[i].substr(common[j][i]);
            if (DP[mask][i].empty() or DP[mask][i].size() > cur.size())
              DP[mask][i] = cur;
          }
        }
      }
    }
    string ret = DP.back()[0];
    for (int i = 1; i < N; ++i)
      if (DP.back()[i].size() < ret.size()) ret = DP.back()[i];
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
