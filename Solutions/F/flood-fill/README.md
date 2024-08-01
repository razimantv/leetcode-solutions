# Flood fill

[Problem link](https://leetcode.com/problems/flood-fill)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/flood-fill

class Solution {
 public:
  void work(vector<vector<int>>& image, int sr, int sc, int c0, int c1) {
    image[sr][sc] = c1;
    if (sr > 0 and image[sr - 1][sc] == c0) work(image, sr - 1, sc, c0, c1);
    if (sr + 1 < image.size() and image[sr + 1][sc] == c0)
      work(image, sr + 1, sc, c0, c1);
    if (sc > 0 and image[sr][sc - 1] == c0) work(image, sr, sc - 1, c0, c1);
    if (sc + 1 < image[0].size() and image[sr][sc + 1] == c0)
      work(image, sr, sc + 1, c0, c1);
  }

  vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc,
                                int newColor) {
    if (image[sr][sc] == newColor) return image;
    auto ret = image;
    work(ret, sr, sc, image[sr][sc], newColor);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
