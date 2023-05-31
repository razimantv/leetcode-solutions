# Stone game vii

[Problem link](https://leetcode.com/problems/stone-game-vii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stone-game-vii

class Solution {
 public:
  int stoneGameVII(vector<int>& stones) {
    int N = stones.size();
    vector<int> psum(N + 1);
    for (int i = 0; i < N; ++i) psum[i + 1] = psum[i] + stones[i];
    vector<vector<int>> DP(N, vector<int>(N));

    for (int L = 1; L < N; ++L)
      for (int i = 0; i + L < N; ++i)
        DP[i][i + L] = max(psum[i + L + 1] - psum[i + 1] - DP[i + 1][i + L],
                           psum[i + L] - psum[i] - DP[i][i + L - 1]);
    return DP[0][N - 1];
  }
};
```