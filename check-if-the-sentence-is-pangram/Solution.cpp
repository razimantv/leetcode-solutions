// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution {
 public:
  bool checkIfPangram(string sentence) {
    vector<int> cnt(26);
    int ret = 0;
    for (char c : sentence)
      if (++cnt[c - 'a'] == 1) ++ret;
    return ret == 26;
  }
};
