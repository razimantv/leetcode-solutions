// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution {
 public:
  vector<int> findAnagrams(string s, string p) {
    map<char, int> pcnt, scnt;
    for (char c : p) pcnt[c]++;

    vector<int> ret;
    for (int l = 0, r = 0; r < s.size(); r++) {
      if (++scnt[s[r]] > pcnt[s[r]]) {
        do {
          --scnt[s[l++]];
        } while (scnt[s[r]] > pcnt[s[r]]);
      }
      if (r - l == p.size() - 1) ret.push_back(l);
    }
    return ret;
  }
};
