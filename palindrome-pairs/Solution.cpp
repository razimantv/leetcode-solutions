// https://leetcode.com/problems/palindrome-pairs

class Solution {
 public:
  vector<vector<int>> palindromePairs(vector<string>& words) {
    const long long P = 31, MOD = 999'999'893;
    vector<int> ppow(301);
    ppow[0] = 1;
    for (int i = 1; i < 301; ++i) ppow[i] = (ppow[i - 1] * P) % MOD;

    vector<int> fwhash, bwhash;
    int W = words.size();
    for (int i = 0; i < W; ++i) {
      int L = words[i].size();

      int cur = 0;
      for (int j = 0; j < L; ++j) cur = (cur * P + words[i][j] - 'a') % MOD;
      fwhash.push_back(cur);

      cur = 0;
      for (int j = L - 1; j >= 0; --j)
        cur = (cur * P + words[i][j] - 'a') % MOD;
      bwhash.push_back(cur);
    }

    vector<vector<int>> ret;
    for (int i = 0; i < W; ++i)
      for (int j = 0; j < W; ++j) {
        if (i == j) continue;
        int hash1 =
            (fwhash[j] + fwhash[i] * (long long)ppow[words[j].size()]) % MOD;
        int hash2 =
            (bwhash[i] + bwhash[j] * (long long)ppow[words[i].size()]) % MOD;
        if (hash1 == hash2) ret.push_back({i, j});
      }
    return ret;
  }
};
