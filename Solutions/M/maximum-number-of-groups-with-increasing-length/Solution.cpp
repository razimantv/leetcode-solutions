// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
 public:
  int maxIncreasingGroups(vector<int>& lim) {
    sort(lim.begin(), lim.end());
    int g{};
    long long tot{};
    for (int x : lim) {
      tot += x;
      if (tot >= ((g + 1ll) * (g + 2)) / 2) ++g;
    }
    return g;
  }
};
