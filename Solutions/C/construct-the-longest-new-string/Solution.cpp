// https://leetcode.com/problems/construct-the-longest-new-string/

class Solution {
 public:
  int longestString(int x, int y, int z) {
    if (x > y) swap(x, y);
    y = min(y, x + 1);
    return 2 * (x + y + z);
  }
};
