// https://leetcode.com/problems/predict-the-winner/

class Solution {
 public:
  // ChatGPT solution
  bool PredictTheWinner(vector<int>& nums) {
    int n = nums.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, -1));
    int scoreDiff = canPlayer1Win(nums, 0, n - 1, dp);
    return scoreDiff >= 0;
  }

  int canPlayer1Win(std::vector<int>& nums, int left, int right,
                    std::vector<std::vector<int>>& dp) {
    if (left == right) {
      return nums[left];
    }
    if (dp[left][right] != -1) {
      return dp[left][right];
    }

    int chooseLeft = nums[left] - canPlayer1Win(nums, left + 1, right, dp);
    int chooseRight = nums[right] - canPlayer1Win(nums, left, right - 1, dp);

    dp[left][right] = std::max(chooseLeft, chooseRight);
    return dp[left][right];
  }
};
