# The number of full rounds you have played

[Problem link](https://leetcode.com/problems/the-number-of-full-rounds-you-have-played)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played

class Solution {
 public:
  pair<int, int> HM(string s) {
    int h = (s[0] - '0') * 10 + s[1] - '0';
    int m = (s[3] - '0') * 10 + s[4] - '0';
    return {h, m};
  }
  int numberOfRounds(string startTime, string finishTime) {
    auto [h1, m1] = HM(startTime);
    auto [h2, m2] = HM(finishTime);

    if (h1 > h2 or (h1 == h2 and m1 > m2)) h2 += 24;
    int ret = (h2 * 4 + m2 / 15) - (h1 * 4 + m1 / 15);
    if ((m1 % 15) and ret) --ret;
    return ret;
  }
};
```