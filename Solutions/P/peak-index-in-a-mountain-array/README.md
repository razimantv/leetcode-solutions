# Peak index in a mountain array

[Problem link](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
 public:
  // ChatGPT solution
  int peakIndexInMountainArray(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
      int mid = left + (right - left) / 2;
      if (arr[mid] > arr[mid + 1]) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  }
};
```
## Tags

* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Binary search](/Collections/binary-search.md#binary-search)
