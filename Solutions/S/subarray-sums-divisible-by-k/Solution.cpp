// https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution {
public:
  int subarraysDivByK(vector<int> &nums, int k) {
    unordered_map<int, int> cnt{{0, 1}};
    int ret{};
    for (int i = 0, s = 0, n = nums.size(); i < n; ++i)
      ret += cnt[s = (s + nums[i] % k + k) % k]++;
    return ret;
  }
};
