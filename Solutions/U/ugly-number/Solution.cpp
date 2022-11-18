// https://leetcode.com/problems/ugly-number/

class Solution {
 public:
  bool isUgly(int n) {
    vector<int> primes{2, 3, 5};
    for (int p : primes)
      while (n and n % p == 0) n /= p;
    return n == 1;
  }
};
