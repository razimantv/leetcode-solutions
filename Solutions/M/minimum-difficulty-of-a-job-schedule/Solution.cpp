// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution {
 public:
  int minDifficulty(vector<int>& jobDifficulty, int d) {
    int n = jobDifficulty.size();
    if (n < d) return -1;
    vector<vector<int>> dp(d + 1, vector<int>(n + 1, 1 << 30));
    dp[0][0] = 0;
    for (int i = 1; i <= d; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int k = j, cur = 0; k >= 0; --k) {
          cur = max(cur, jobDifficulty[k]);
          dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][k] + cur);
        }
      }
    }
    return dp.back().back();
  }
};
