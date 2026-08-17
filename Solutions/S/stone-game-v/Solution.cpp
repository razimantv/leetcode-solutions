// https://leetcode.com/problems/stone-game-v/

class Solution {
  vector<vector<int>> memo;
  vector<int> psum;

  int dp(int l, int r) {
    if (l == r)
      return 0;

    if (memo[l][r] != -1)
      return memo[l][r];

    int max_score = 0;

    for (int m = l; m < r; ++m) {
      int lsum = psum[m + 1] - psum[l], rsum = psum[r + 1] - psum[m + 1];

      if (lsum < rsum) {
        max_score = max(max_score, lsum + dp(l, m));
      } else if (rsum < lsum) {
        max_score = max(max_score, rsum + dp(m + 1, r));
      } else {
        max_score = max(max_score, lsum + max(dp(l, m), dp(m + 1, r)));
      }
    }

    return memo[l][r] = max_score;
  }

public:
  int stoneGameV(vector<int> &stones) {
    int n = stones.size();
    memo.assign(n, vector<int>(n, -1));

    psum.assign(n + 1, 0);
    for (int i = 0; i < n; ++i)
      psum[i + 1] = psum[i] + stones[i];

    return dp(0, n - 1);
  }
};
