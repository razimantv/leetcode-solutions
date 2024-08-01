# Can make arithmetic progression from sequence

[Problem link](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution {
 public:
  // ChatGPT solution
  bool canMakeArithmeticProgression(vector<int>& arr) {
    std::sort(arr.begin(), arr.end());
    int diff = arr[1] - arr[0];
    for (int i = 2; i < arr.size(); i++) {
      if (arr[i] - arr[i - 1] != diff) {
        return false;
      }
    }
    return true;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
