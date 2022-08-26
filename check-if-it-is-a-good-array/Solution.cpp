// https://leetcode.com/problems/check-if-it-is-a-good-array

class Solution {
 public:
  bool isGoodArray(vector<int>& nums) {
    int g = 0;
    for (int n : nums)
      if ((g = __gcd(g, n)) == 1) return true;
    return false;
  }
};
