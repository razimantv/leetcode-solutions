# Put marbles in bags

[Problem link](https://leetcode.com/problems/put-marbles-in-bags/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/put-marbles-in-bags/

class Solution {
 public:
  long long putMarbles(vector<int>& weights, int k) {
    vector<int> pair;
    for (int i = 1, n = weights.size(); i < n; ++i)
      pair.push_back(weights[i - 1] + weights[i]);
    sort(pair.begin(), pair.end());
    --k;
    return accumulate(pair.end() - k, pair.end(), 0ll) -
           accumulate(pair.begin(), pair.begin() + k, 0ll);
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
