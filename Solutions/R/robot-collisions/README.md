# Robot collisions

[Problem link](https://leetcode.com/problems/robot-collisions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/robot-collisions/

class Solution {
 public:
  vector<int> survivedRobotsHealths(vector<int>& positions,
                                    vector<int>& healths, string directions) {
    int n = positions.size();
    vector<int> indices(n), left(n, -1), right(n, -1), survived(n, 1);
    iota(indices.begin(), indices.end(), 0);
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return positions[i] < positions[j]; });

    set<tuple<int, int, int>> collisions;
    for (int i = 1; i < n; ++i) {
      int i1 = indices[i - 1], i2 = indices[i];
      left[i2] = i1;
      right[i1] = i2;
      if (directions[i1] == 'R' and directions[i2] == 'L') {
        collisions.insert({positions[i2] - positions[i1], i1, i2});
      }
    }

    while (!collisions.empty()) {
      auto [t, i1, i2] = *collisions.begin();
      collisions.erase(collisions.begin());

      int l = left[i1], r = right[i2];
      if (healths[i1] == healths[i2]) {
        survived[i1] = survived[i2] = 0;
        if (l != -1) right[l] = r;
        if (r != -1) left[r] = l;
        if (l != -1 and r != -1 and directions[l] == 'R' and
            directions[r] == 'L')
          collisions.insert({positions[r] - positions[l], l, r});
      } else if (healths[i1] > healths[i2]) {
        survived[i2] = 0;
        --healths[i1];
        if (r != -1) left[r] = i1;
        if (r != -1 and directions[r] == 'L')
          collisions.insert({positions[r] - positions[i1], i1, r});
      } else {
        survived[i1] = 0;
        --healths[i2];
        if (l != -1) right[l] = i2;
        if (l != -1 and directions[l] == 'R')
          collisions.insert({positions[i2] - positions[l], l, i2});
      }
    }

    vector<int> ret;
    for (int i = 0; i < n; ++i)
      if (survived[i]) ret.push_back(healths[i]);
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Dynamic update of left and right neighbours](/Collections/dynamic-update-of-left-and-right-neighbours.md#dynamic-update-of-left-and-right-neighbours)
