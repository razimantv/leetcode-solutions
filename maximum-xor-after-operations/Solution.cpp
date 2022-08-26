// https://leetcode.com/problems/maximum-xor-after-operations

class Solution {
 public:
  int maximumXOR(vector<int>& nums) {
    int ret = 0;
    for (int x : nums) ret |= x;
    return ret;
  }
};
