// https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution {
 public:
  int distinctIntegers(int n) { return n - 1 + (n == 1); }
};
