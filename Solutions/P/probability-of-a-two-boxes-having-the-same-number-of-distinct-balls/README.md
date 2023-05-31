# Probability of a two boxes having the same number of distinct balls

[Problem link](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls

class Solution {
 public:
  double getProbability(vector<int>& balls) {
    int N = balls.size(), M = accumulate(balls.begin(), balls.end(), 0);

    vector<double> factorial(M + 1);
    factorial[0] = 1;
    for (int i = 1; i <= M; ++i) factorial[i] = factorial[i - 1] * i;

    double tot = factorial[M];
    for (int n : balls) tot /= factorial[n];

    vector<int> cur(N);
    double good = 0;
    while (1) {
      bool flag = false;
      for (int i = 0; i < N; ++i) {
        if (++cur[i] > balls[i])
          cur[i] = 0;
        else {
          flag = true;
          break;
        }
      }
      if (!flag) break;

      double cnt = factorial[M >> 1];
      cnt *= cnt;
      int diff = 0, x = 0;
      for (int i = 0; i < N; ++i) {
        diff += (cur[i] > 0) - (cur[i] < balls[i]);
        cnt /= factorial[cur[i]] * factorial[balls[i] - cur[i]];
        x += cur[i];
      }
      if (x == M / 2 and diff == 0) good += cnt;
    }
    return good / tot;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Probability](/README.md#Mathematics-Probability)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Brute force enumeration](/README.md#Brute_force_enumeration) > [Combinatorial](/README.md#Brute_force_enumeration-Combinatorial)
