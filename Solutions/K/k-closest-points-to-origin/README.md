# K closest points to origin

[Problem link](https://leetcode.com/problems/k-closest-points-to-origin)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/k-closest-points-to-origin

class Solution {
 public:
  vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
    nth_element(points.begin(), points.begin() + K, points.end(),
                [](const vector<int>& u, const vector<int>& v) -> bool {
                  return u[0] * u[0] + u[1] * u[1] < v[0] * v[0] + v[1] * v[1];
                });
    points.resize(K);
    return points;
  }
};
```
## Tags

* [Sorting](/README.md#Sorting) > [Custom](/README.md#Sorting-Custom)
* [Sorting](/README.md#Sorting) > [Partial](/README.md#Sorting-Partial)
