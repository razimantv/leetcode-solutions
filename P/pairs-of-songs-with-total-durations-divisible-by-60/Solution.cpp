// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution {
 public:
  int numPairsDivisibleBy60(vector<int>& time) {
    vector<int> cnt(60);
    int ret = 0;
    for (int t : time) {
      t %= 60;
      ret += cnt[t == 0 ? 0 : 60 - t];
      ++cnt[t];
    }
    return ret;
  }
};
