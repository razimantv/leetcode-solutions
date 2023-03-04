// https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution {
 public:
  long long coloredCells(int n) {
    return n * (long long)n + (n - 1) * (long long)(n - 1);
  }
};
