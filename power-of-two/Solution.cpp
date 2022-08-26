// https://leetcode.com/problems/power-of-two

class Solution {
 public:
  bool isPowerOfTwo(int n) { return n > 0 and !(n & (n - 1)); }
};
