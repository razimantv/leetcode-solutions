// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros

class Solution {
 public:
  bool checkZeroOnes(string s) {
    int cnt[2] = {0, 0};
    for (int i = 0, cur = 0;; ++i) {
      if (i == 0 or s[i] == s[i - 1])
        ++cur;
      else {
        cnt[s[i - 1] - '0'] = max(cnt[s[i - 1] - '0'], cur);
        cur = 1;
      }
      if (!s[i]) break;
    }
    return cnt[1] > cnt[0];
  }
};
