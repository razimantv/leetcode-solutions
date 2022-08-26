// https://leetcode.com/problems/count-primes

class Solution {
 public:
  int countPrimes(int n) {
    if (--n < 4) return max(0, n - 1);
    int N = (n >> 6) + 1, n2 = (n >> 1);
    unsigned int *notprime = new unsigned int[N];
    memset(notprime, 0, N << 2);

    for (int i = 3, ii = 1; i * i <= n; i += 2, ++ii) {
      if (notprime[ii >> 5] & (1u << (ii & 31))) continue;
      for (int j = (i * i) >> 1; j <= n2; j += i)
        notprime[j >> 5] |= (1u << (j & 31));
    }
    for (int i = n + 1 + (n & 1); i < (N << 6); i += 2)
      notprime[i >> 6] &= ~(1u << ((i >> 1) & 31));

    int ret = 0;
    for (int i = 0; i < N; ++i) ret += __builtin_popcount(notprime[i]);
    return n - n / 2 - ret;
  }
};
