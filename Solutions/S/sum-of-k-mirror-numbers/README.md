# Sum of k mirror numbers

[Problem link](https://leetcode.com/problems/sum-of-k-mirror-numbers/)

## Observations

- A number is a "k-mirror" number if it's palindromic in both base 10 and base `k`.
- The problem asks for the sum of the first `n` such numbers.
- The numbers can get very large, so iterating through all numbers and checking the two palindrome conditions would be too slow.
- It's much more efficient to *generate* palindromic numbers in one base and then *test* if they are palindromic in the other.
- Since base 10 representations are easier to work with in code, the strategy is to generate base-10 palindromes and then check if they are also palindromes in base `k`.

## Algorithm

The algorithm generates base-10 palindromes in increasing order and, for each one, checks if its base-`k` representation is also a palindrome. It stops after finding and summing `n` such numbers.

1.  **Generate Base-10 Palindromes**:
    -   The code generates palindromes by taking a number, converting it to a string, and appending its reverse.
    -   It handles both even-length and odd-length palindromes.
        -   For a number `i` (e.g., `123`), it creates an even-length palindrome by `s + s_reversed` (e.g., `"123" + "321"` -> `123321`).
        -   It creates an odd-length palindrome by `s + s_reversed_without_first_char` (e.g., `"123" + "21"` -> `12321`).
    -   The generation happens in batches based on the number of digits. It starts with 1-digit numbers (`i` from 1 to 9), then 2-digit numbers (`i` from 10 to 99), and so on. This ensures the generated palindromes are found in increasing order.

2.  **Check Base-k Palindrome (`isgood` function)**:
    -   This function takes an integer `n` and checks if its representation in base `k` is a palindrome.
    -   It does this by repeatedly taking the number modulo `k` to get the last digit and then integer-dividing by `k` to remove the last digit.
    -   The digits are stored in a list.
    -   Finally, it checks if the list of digits is the same as its reverse.

3.  **Main Loop**:
    -   The main loop continues until `n` k-mirror numbers have been found.
    -   It iterates through ranges of numbers (`start` to `end`, e.g., 1-10, 10-100, etc.) to generate the "half" of the palindromes.
    -   For each generated base-10 palindrome `cur`, it calls `isgood(cur)` to test the base-`k` condition.
    -   If `isgood(cur)` is true, the number is added to the running sum `ret`, and the count `n` is decremented.
    -   The loop terminates and returns `ret` as soon as `n` reaches zero.

## Complexity

-   **Time Complexity**: The complexity is difficult to express in a simple formula, as it depends on the distribution of k-mirror numbers. The process generates base-10 palindromes and for each, performs a base conversion that takes `O(log_k(m))`, where `m` is the value of the palindrome. Since we only need to find 30 such numbers, the generation doesn't go on for too long.

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isgood(n):
            num = []
            while n:
                num.append(n % k)
                n //= k
            return num == num[::-1]

        start, end, ret = 1, 10, 0
        while n:
            for skip in [1, 0]:
                for i in range(start, end):
                    s = str(i)
                    cur = int(s + s[::-1][skip:])
                    if isgood(cur):
                        ret += cur
                        n -= 1
                        if not n:
                            return ret
            start, end = end, end * 10
        return ret
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
