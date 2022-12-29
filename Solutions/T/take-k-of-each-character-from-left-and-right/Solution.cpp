// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution {
 public:
  int takeCharacters(string s, int k) {
    if (!k) return 0;
    int n = s.size();

    vector<int> cur(3);

    unordered_map<int, int> first[3];
    for (int i = 0; i < n; ++i) {
      char c = s[i] - 'a';
      first[c][++cur[c]] = i + 1;
    }

    for (int& x : cur) {
      if (x < k) return -1;
      x = 0;
    }

    int ret = n;
    for (int i = n; i >= 0; --i) {
      if (i < n) {
        char c = s[i] - 'a';
        ++cur[c];
      }
      int x = 0;
      for (int j = 0; j < 3; ++j)
        x = max(x, n - i + first[j][max(0, k - cur[j])]);
      ret = min(ret, x);
    }
    return ret;
  }
};
