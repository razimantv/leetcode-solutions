# Transform to chessboard

[Problem link](https://leetcode.com/problems/transform-to-chessboard)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/transform-to-chessboard

class Solution {
 public:
  int movesToChessboard(vector<vector<int>>& b) {
    int N = b.size(), rowSum = 0, colSum = 0, rowSwap = 0, colSwap = 0;
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j)
        if (b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j]) return -1;
    for (int i = 0; i < N; ++i) {
      rowSum += b[0][i];
      colSum += b[i][0];
      rowSwap += b[i][0] == i % 2;
      colSwap += b[0][i] == i % 2;
    }
    if (rowSum != N / 2 && rowSum != (N + 1) / 2) return -1;
    if (colSum != N / 2 && colSum != (N + 1) / 2) return -1;
    if (N % 2) {
      if (colSwap % 2) colSwap = N - colSwap;
      if (rowSwap % 2) rowSwap = N - rowSwap;
    } else {
      colSwap = min(N - colSwap, colSwap);
      rowSwap = min(N - rowSwap, rowSwap);
    }
    return (colSwap + rowSwap) / 2;
  }
};
```