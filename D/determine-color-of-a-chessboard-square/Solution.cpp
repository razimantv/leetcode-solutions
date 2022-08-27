// https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution {
 public:
  bool squareIsWhite(string c) { return ((c[0] - 'a') + (c[1] - '1')) & 1; }
};
