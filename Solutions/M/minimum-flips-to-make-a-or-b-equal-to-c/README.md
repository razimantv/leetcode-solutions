# Minimum flips to make a or b equal to c

[Problem link](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution {
 public:
  // ChatGPT solution
  int minFlips(int a, int b, int c) {
    int flips = 0;

    for (int i = 0; i < 32; i++) {
      int bit_a = (a >> i) & 1;
      int bit_b = (b >> i) & 1;
      int bit_c = (c >> i) & 1;

      if ((bit_a | bit_b) != bit_c) {
        if (bit_c == 1) {
          flips++;
        } else {
          if (bit_a == 1) {
            flips++;
          }
          if (bit_b == 1) {
            flips++;
          }
        }
      }
    }

    return flips;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
