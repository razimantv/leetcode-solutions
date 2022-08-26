// https://leetcode.com/problems/number-of-matching-subsequences

class Solution {
 public:
  int numMatchingSubseq(string s, vector<string>& words) {
    int W = words.size();
    vector<pair<int, int>> nextchar[26];
    for (int i = 0; i < W; ++i) nextchar[words[i][0] - 'a'].push_back({i, 0});

    int ret = 0;
    for (int i = 0; s[i]; ++i) {
      char c = s[i] - 'a';
      auto cur = nextchar[c];
      nextchar[c].clear();

      for (auto [id, pos] : cur) {
        if (!words[id][++pos])
          ++ret;
        else
          nextchar[words[id][pos] - 'a'].push_back({id, pos});
      }
    }
    return ret;
  }
};
