// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
 public:
  bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    if (sx == fx and sy == fy and t == 1) return false;
    long long dx = abs(sx - fx), dy = abs(sy - fy);
    return max(dx, dy) <= t;
  }
};
