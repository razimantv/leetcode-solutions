// https://leetcode.com/problems/jump-game-iii

class Solution {
 public:
  bool canReach(vector<int>& arr, int u) {
    if (!arr[u])
      return true;
    else if (arr[u] < 0)
      return false;

    int j = arr[u];
    arr[u] = -j;

    if (u >= j and canReach(arr, u - j)) return true;
    if (u + j < arr.size() and canReach(arr, u + j)) return true;
    return false;
  }
};
