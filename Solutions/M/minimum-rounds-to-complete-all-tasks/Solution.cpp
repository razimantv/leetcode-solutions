// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

class Solution {
 public:
  int minimumRounds(vector<int>& tasks) {
    unordered_map<int, int> cnt;
    for (int t : tasks) ++cnt[t];
    int ret{};
    for (auto [k, v] : cnt) {
      if (v == 1) return -1;
      ret += (v / 3) + (v % 3 > 0);
    }
    return ret;
  }
};
