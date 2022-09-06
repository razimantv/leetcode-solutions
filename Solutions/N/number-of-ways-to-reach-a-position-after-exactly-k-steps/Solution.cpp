// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution {
 public:
  int numberOfWays(int s, int e, int k) {
    int r = abs(s - e);
    if (r > k or ((k - r) & 1)) return 0;
    vector<int> ncr(k + 1, 1);
    for (int i = 1; i <= k; ++i) {
      for (int j = i - 1; j; --j)
        ncr[j] = (ncr[j] + ncr[j - 1]) % 1'000'000'007;
    }
    return ncr[(k + r) >> 1];
  }
};
