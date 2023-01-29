// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
 public:
  const int MOD = 1'000'000'007;
  long long pow(long long a, int b) {
    long long ret = 1;
    while (b) {
      if (b & 1) ret = (ret * a) % MOD;
      a = (a * a) % MOD;
      b >>= 1;
    }
    return ret;
  }
  int monkeyMove(int n) { return (pow(2, n) + MOD - 2) % MOD; }
};
