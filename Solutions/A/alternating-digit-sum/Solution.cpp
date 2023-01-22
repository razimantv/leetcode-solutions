// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
 public:
  int alternateDigitSum(int n) {
    int ret{};
    while (n) ret = n % 10 - ret, n /= 10;
    return ret;
  }
};
