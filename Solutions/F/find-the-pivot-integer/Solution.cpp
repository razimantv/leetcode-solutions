// https://leetcode.com/problems/find-the-pivot-integer/

class Solution {
 public:
  int pivotInteger(int n) {
    int a = n * (n + 1) / 2;
    for (int i = 1; i <= n; ++i)
      if (i * (i + 1) / 2 == a - i * (i - 1) / 2) return i;
    return -1;
  }
};
