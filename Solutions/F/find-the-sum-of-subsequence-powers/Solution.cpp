// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

const int mod = 1'000'000'007;

void inc(int& x, int y) {
  x += y;
  if (x >= mod) x -= mod;
}

class Solution {
 public:
  int sumOfPowers(vector<int>& nums, int K) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    unordered_set<int> diffs;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j) diffs.insert(nums[i] - nums[j]);
    int ret = 0;
    for (auto d : diffs) {
      vector<vector<vector<int>>> dp(
          n, vector<vector<int>>(K + 1, vector<int>(2, 0))
      );
      for (int i = 0; i < n; ++i) {
        int x = nums[i];
        dp[i][1][0] = 1;
        for (int ii = 0; ii < i; ++ii) {
          int dd = x - nums[ii];
          if (dd < d) break;
          if (dd == d) {
            for (int k = 2; k <= K; ++k) {
              inc(dp[i][k][1], dp[ii][k - 1][0]);
              inc(dp[i][k][1], dp[ii][k - 1][1]);
            }
          } else {
            for (int k = 2; k <= K; ++k) {
              inc(dp[i][k][0], dp[ii][k - 1][0]);
              inc(dp[i][k][1], dp[ii][k - 1][1]);
            }
          }
        }
        ret = (ret + dp[i][K][1] * 1ll * d) % mod;
      }
    }
    return ret;
  }
};
