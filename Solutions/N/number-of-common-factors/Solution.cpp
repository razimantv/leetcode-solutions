// https://leetcode.com/problems/number-of-common-factors/

class Solution {
 public:
  int commonFactors(int a, int b) {
    int g = __gcd(a, b), ret = 0;
    for (int i = 1; i <= g; ++i)
      if (g % i == 0) ++ret;
    return ret;
  }
};
