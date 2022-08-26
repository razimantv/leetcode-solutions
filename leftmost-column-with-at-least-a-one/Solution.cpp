// https://leetcode.com/problems/leftmost-column-with-at-least-a-one

/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int row, int col);
 *     vector<int> dimensions();
 * };
 */
class Solution {
 public:
  int leftMostColumnWithOne(BinaryMatrix &b) {
    auto dim = b.dimensions();
    int r = dim[0], c = dim[1];
    int ret = c - 1;
    for (int i = 0; i < r; ++i) {
      for (; ret >= 0 and b.get(i, ret); ret--)
        ;
    }
    if (ret + 1 == c) return -1;
    return ret + 1;
  }
};
