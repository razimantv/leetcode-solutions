// https://leetcode.com/problems/smallest-even-multiple/

class Solution {
 public:
  int smallestEvenMultiple(int n) { return (n & 1) ? (n * 2) : n; }
};
