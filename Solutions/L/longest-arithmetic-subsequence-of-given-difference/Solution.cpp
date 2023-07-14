// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution {
 public:
  // ChatGPT solution
  int longestSubsequence(vector<int>& arr, int difference) {
    std::unordered_map<int, int> dp;
    int maxLength = 0;

    for (int num : arr) {
      if (dp.count(num - difference)) {
        dp[num] = dp[num - difference] + 1;
      } else {
        dp[num] = 1;
      }

      maxLength = std::max(maxLength, dp[num]);
    }

    return maxLength;
  }
};
