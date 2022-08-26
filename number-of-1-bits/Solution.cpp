// https://leetcode.com/problems/number-of-1-bits

class Solution {
 public:
  int hammingWeight(uint32_t n) { return __builtin_popcount(n); }
};
