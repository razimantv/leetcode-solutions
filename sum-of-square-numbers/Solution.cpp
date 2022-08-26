// https://leetcode.com/problems/sum-of-square-numbers

class Solution {
 public:
  bool judgeSquareSum(int c) {
    for (int i = 2; i < 65536 and i * i <= c; ++i) {
      if (c % i) continue;
      int cnt = 0;
      while (c % i == 0) ++cnt, c /= i;
      if ((i & 3) == 3 and (cnt & 1)) return false;
    }
    if ((c & 3) == 3) return false;
    return true;
  }
};
