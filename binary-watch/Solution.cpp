// https://leetcode.com/problems/binary-watch

class Solution {
 public:
  vector<string> readBinaryWatch(int turnedOn) {
    char wut[10];
    vector<string> ret;
    for (int i = 0; i < 12; ++i)
      for (int j = 0; j < 60; ++j)
        if (__builtin_popcount(i) + __builtin_popcount(j) == turnedOn) {
          sprintf(wut, "%d:%02d", i, j);
          ret.push_back(wut);
        }
    return ret;
  }
};
