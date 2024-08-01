# Sum of number and its reverse

[Problem link](https://leetcode.com/problems/sum-of-number-and-its-reverse/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution {
public:
 int rev(int n) {
   int ret = 0;
   while (n) {
     ret = ret * 10 + n % 10;
     n /= 10;
   }
   return ret;
 }
 bool sumOfNumberAndReverse(int num) {
   for (int i = 0; i <= num; ++i) {
     if (i + rev(i) == num) return true;
   }
   return false;
 }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
