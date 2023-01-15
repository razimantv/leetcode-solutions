// https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution {
 public:
  long long countGood(vector<int>& nums, int k) {
    long long ret{};
    unordered_map<int, int> cnt;
    for (int i = 0, j = -1, n = nums.size(), tot = 0; i < n; ++i) {
      while (tot < k and j < n - 1) tot += cnt[nums[++j]]++;
      if (tot >= k)
        ret += n - j;
      else
        break;
      tot -= --cnt[nums[i]];
    }
    return ret;
  }
};
