# Construct quad tree

[Problem link](https://leetcode.com/problems/construct-quad-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-quad-tree/

class Solution {
 public:
  Node* construct(vector<vector<int>>& grid) {
    int n = grid.size();
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        grid[i][j] += (i ? grid[i - 1][j] : 0) + (j ? grid[i][j - 1] : 0) -
                      ((i && j) ? grid[i - 1][j - 1] : 0);

    function<Node*(int, int, int)> work = [&](int i, int j, int x) {
      int ip = i + x - 1, jp = j + x - 1;
      int tot = grid[ip][jp] - (i ? grid[i - 1][jp] : 0) -
                (j ? grid[ip][j - 1] : 0) + ((i && j) ? grid[i - 1][j - 1] : 0);
      Node* ret = new Node;
      for (int val : {0, 1}) {
        if (tot == x * x * val) {
          ret->val = val;
          ret->isLeaf = true;
          return ret;
        }
      }

      int xc = x >> 1;
      ret->topLeft = work(i, j, xc);
      ret->topRight = work(i, j + xc, xc);
      ret->bottomLeft = work(i + xc, j, xc);
      ret->bottomRight = work(i + xc, j + xc, xc);
      return ret;
    };
    return work(0, 0, n);
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [QuadTree](/Collections/quadtree.md#quadtree)
