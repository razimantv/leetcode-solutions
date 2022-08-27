// https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution {
 public:
  int minOperations(int n) { return (n - n / 2) * (n / 2); }
};
