// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
 public:
  long long maxScore(vector<int>& nums, int x) {
    long long best[2]{0ll, 0ll};
    for (int n = nums.size(), i = n - 1; i >= 0; --i) {
      int y = nums[i], b = y & 1, c = b ^ 1;
      best[b] = y + max(best[b], max(0ll, best[c] - x));
    }
    return best[nums[0] & 1];
  }
};
