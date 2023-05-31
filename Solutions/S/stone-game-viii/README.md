# Stone game viii

[Problem link](https://leetcode.com/problems/stone-game-viii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stone-game-viii

class Solution {
 public:
  int stoneGameVIII(vector<int>& stones) {
    int N = stones.size();
    vector<int> psum(N), alice(N), bob(N), bestbob(N), bestalice(N);
    psum[0] = stones[0];
    for (int i = 1; i < N; ++i) psum[i] = psum[i - 1] + stones[i];

    alice[N - 2] = psum[N - 1];
    bob[N - 2] = -psum[N - 1];
    bestalice[N - 2] = alice[N - 2] - psum[N - 2];
    bestbob[N - 2] = bob[N - 2] + psum[N - 2];

    // for (int i = N - 3; i >= 0; --i) {
    // alice[i] = psum[N - 1];
    // bob[i] = -psum[N - 1];
    // for (int j = i + 1; j < N - 1; ++j) {
    // alice[i] = max(alice[i], psum[j] + bob[j]);
    // bob[i] = min(bob[i], alice[j] - psum[j]);
    //}
    //}
    for (int i = N - 3; i >= 0; --i) {
      alice[i] = max(psum[N - 1], bestbob[i + 1]);
      bob[i] = min(-psum[N - 1], bestalice[i + 1]);

      bestalice[i] = min(bestalice[i + 1], alice[i] - psum[i]);
      bestbob[i] = max(bestbob[i + 1], psum[i] + bob[i]);
    }

    return alice[0];
  }
};
```