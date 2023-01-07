// https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution {
 public:
  int xorBeauty(vector<int>& nums) {
    int ret{};
    long long n = nums.size();
    for (int i = 0; i < 31; ++i) {
      long long cur{};
      for (int x : nums)
        if (x & (1 << i)) ++cur;
      long long ways = cur * (n * n - (n - cur) * (n - cur));
      if (ways & 1) ret ^= 1 << i;
    }
    return ret;
  }
};
