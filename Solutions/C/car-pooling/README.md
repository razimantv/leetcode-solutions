# Car pooling

[Problem link](https://leetcode.com/problems/car-pooling)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/car-pooling

class Solution {
 public:
  bool carPooling(vector<vector<int>>& trips, int capacity) {
    vector<vector<int>> endpoints;
    for (auto& trip : trips) {
      endpoints.push_back({trip[1], trip[0]});
      endpoints.push_back({trip[2], -trip[0]});
    }
    sort(endpoints.begin(), endpoints.end());

    int cur = 0;
    for (auto& ep : endpoints) {
      if ((cur += ep[1]) > capacity) return false;
    }
    return true;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Endpoint sorting](/Collections/intervals.md#endpoint-sorting)
