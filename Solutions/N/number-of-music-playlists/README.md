# Number of music playlists

[Problem link](https://leetcode.com/problems/number-of-music-playlists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-music-playlists

class Solution {
 public:
  // ChatGPT solution (needed fix)
  int numMusicPlaylists(int n, int goal, int k) {
    const int MOD = 1e9 + 7;
    std::vector<std::vector<int>> dp(goal + 1, std::vector<int>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= goal; ++i) {
      for (int j = 1; j <= n; ++j) {
        dp[i][j] = (1LL * dp[i - 1][j - 1] * j +
                    1LL * dp[i - 1][j] * std::max(j - k, 0)) %
                   MOD;
      }
    }

    return dp[goal][n];
  }
};
```
## Tags

* [ChatGPT](/Collections/chatgpt.md#chatgpt) > [Fixed](/Collections/chatgpt.md#fixed)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
