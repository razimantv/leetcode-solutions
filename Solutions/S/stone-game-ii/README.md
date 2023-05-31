# Stone game ii

[Problem link](https://leetcode.com/problems/stone-game-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stone-game-ii

class Solution {
 public:
  unordered_map<int, int> cache;
  int work(const vector<int>& piles, int i, int M) {
    if (2 * M >= piles.size() - i) M = (piles.size() - i + 1) / 2;
    {
      auto mit = cache.find(i * 1000 + M);
      if (mit != cache.end()) return mit->second;
    }
    if (2 * M >= piles.size() - i)
      return cache[i * 1000 + M] =
                 accumulate(piles.begin() + i, piles.end(), 0);

    int ret = piles[i] - work(piles, i + 1, M);
    for (int m = 2, cur = piles[i]; m <= 2 * M and i + m < piles.size(); ++m)
      ret = max(ret, (cur += piles[i + m - 1]) - work(piles, i + m, max(M, m)));
    return cache[i * 1000 + M] = ret;
  }
  int stoneGameII(const vector<int>& piles) {
    return (work(piles, 0, 1) + work(piles, 0, piles.size())) / 2;
  }
};
```