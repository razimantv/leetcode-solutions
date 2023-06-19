// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
 public:
  int largestAltitude(vector<int>& gain) {
    int ret{}, pref{};
    for (int x : gain) ret = max(ret, pref += x);
    return ret;
  }
};
