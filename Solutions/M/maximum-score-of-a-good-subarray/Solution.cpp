// https://leetcode.com/problems/maximum-score-of-a-good-subarray

class Solution {
 public:
  int maximumScore(vector<int>& nums, int k) {
    nums.push_back(-1);
    int N = nums.size(), best = 0;
    vector<int> s{-1};

    for (int i = 0, u; i < N; ++i) {
      while (s.back() != -1 and nums[u = s.back()] >= nums[i]) {
        s.pop_back();
        if (s.back() < k and i > k)
          best = max(best, nums[u] * (i - s.back() - 1));
      }
      s.push_back(i);
    }

    return best;
  }
};
