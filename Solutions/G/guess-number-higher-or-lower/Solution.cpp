// https://leetcode.com/problems/guess-number-higher-or-lower

class Solution {
 public:
  int guessNumber(int r, long long l = 0) {
    while (r - l > 1) {
      auto m = (r + l) >> 1;
      int x = guess(m);
      if (x == 0)
        return m;
      else if (x == -1)
        r = m;
      else
        l = m;
    }
    return r;
  }
};
