// https://leetcode.com/problems/pass-the-pillow/

class Solution {
 public:
  int passThePillow(int n, int time, int cur = 1, int dir = 1) {
    if (time == 0) return cur;
    if ((dir == 1 and cur == n) or (dir == -1 and cur == 1)) dir = -dir;
    return passThePillow(n, time - 1, cur + dir, dir);
  }
};
