// https://leetcode.com/problems/valid-perfect-square

class Solution {
 public:
  bool isPerfectSquare(int num) {
    int sub = -1;
    while (num > 0) num -= (sub += 2);
    return num == 0;
  }
};
