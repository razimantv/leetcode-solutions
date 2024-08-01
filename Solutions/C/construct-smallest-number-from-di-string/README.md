# Construct smallest number from di string

[Problem link](https://leetcode.com/problems/construct-smallest-number-from-di-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution {
 public:
  string smallestNumber(string pattern) {
    int N = pattern.size();
    vector<unordered_map<int, int>> DP(N + 1);
    for (int i = 1; i <= 9; ++i) DP[0][(i << 20) | (1 << i)] = i;
    for (int i = 0; i < N; ++i) {
      for (auto [k, v] : DP[i]) {
        int last = k >> 20, start, end;
        if (pattern[i] == 'I')
          start = last + 1, end = 9;
        else
          start = 1, end = last - 1;
        for (int j = start; j <= end; ++j) {
          if (k & (1 << j)) continue;
          int nextmask = k ^ ((last ^ j) << 20) ^ (1 << j),
              nextval = v * 10 + j;
          if (!DP[i + 1].count(nextmask))
            DP[i + 1][nextmask] = nextval;
          else
            DP[i + 1][nextmask] = min(DP[i + 1][nextmask], nextval);
        }
      }
    }

    int best = INT_MAX;
    for (auto [k, v] : DP.back()) best = min(best, v);
    return to_string(best);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
