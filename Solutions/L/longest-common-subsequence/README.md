# Longest common subsequence

[Problem link](https://leetcode.com/problems/longest-common-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-common-subsequence

class Solution {
 public:
  int longestCommonSubsequence(string text1, string text2) {
    int M = text1.size(), N = text2.size();
    vector<vector<int>> best(M + 1, vector<int>(N + 1, 0));
    for (int i = 0; i < M; i++)
      for (int j = 0; j < N; j++)
        if (text1[i] == text2[j])
          best[i + 1][j + 1] = best[i][j] + 1;
        else
          best[i + 1][j + 1] = max(best[i][j + 1], best[i + 1][j]);
    return best[M][N];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest common subsequence](/Collections/dynamic-programming.md#longest-common-subsequence)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
