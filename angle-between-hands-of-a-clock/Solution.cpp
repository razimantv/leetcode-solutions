// https://leetcode.com/problems/angle-between-hands-of-a-clock

class Solution {
 public:
  double angleClock(int h, int m) {
    double ret = abs(m * 5.5 - h * 30);
    if (ret > 180) ret = 360 - ret;
    return ret;
  }
};
