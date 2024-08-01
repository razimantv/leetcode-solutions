# Erect the fence

[Problem link](https://leetcode.com/problems/erect-the-fence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/erect-the-fence

typedef vector<int> Vec2;

int norm2(const Vec2 &v) { return v[0] * v[0] + v[1] * v[1]; }
Vec2 add(const Vec2 &a, const Vec2 &b) { return {a[0] + b[0], a[1] + b[1]}; }
Vec2 sub(const Vec2 &a, const Vec2 &b) { return {a[0] - b[0], a[1] - b[1]}; }
int dot(const Vec2 &a, const Vec2 &b) { return a[0] * b[0] + a[1] * b[1]; }
double proj(const Vec2 &a, const Vec2 &b) { return dot(a, b) / sqrt(norm2(b)); }
int cross(const Vec2 &a, const Vec2 &b) { return a[0] * b[1] - a[1] * b[0]; }
bool clockwise(Vec2 &A, Vec2 &B, Vec2 &C) {
  return cross(sub(B, A), sub(C, B)) < 0;
}

vector<Vec2> convexHull(vector<Vec2> &P) {
  int n = P.size(), k = 0;
  vector<Vec2> H(2 * n);
  sort(P.begin(), P.end());
  // Build lower hull
  for (int i = 0; i < n; i++) {
    while (k >= 2 && clockwise(H[k - 2], H[k - 1], P[i])) k--;
    H[k++] = P[i];
  }
  // Build upper hull
  for (int i = n - 2, t = k + 1; i >= 0; i--) {
    while (k >= t && clockwise(H[k - 2], H[k - 1], P[i])) k--;
    H[k++] = P[i];
  }
  H.resize(k - 1);

  for (int i = 0; i < H.size(); ++i) {
    for (int j = 0; j < i; ++j) {
      if (H[i] == H[j]) {
        swap(H[i--], H.back());
        H.pop_back();
        break;
      }
    }
  }
  return H;
}

class Solution {
 public:
  vector<vector<int>> outerTrees(vector<vector<int>> &trees) {
    if (trees.size() < 4) return trees;
    return convexHull(trees);
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry) > [Convex hull](/Collections/mathematics.md#convex-hull)
