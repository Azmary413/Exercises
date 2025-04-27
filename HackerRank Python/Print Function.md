# Python Print Function Problem

## Problem Statement

The provided code stub reads an integer `n` from standard input.

Without using any **string methods**, print the numbers from `1` to `n` **consecutively** on a single line (no spaces in between).

---

## Input Format

- A single line containing the integer `n`.

## Constraints

- 1 ≤ n < 150

## Output Format

- Print the numbers from `1` to `n`, each immediately following the previous number, without any space.

---

## Sample Input 0
```
3
```

## Sample Output 0
```
123
```

### Explanation:
- We need to print numbers from 1 to 3 without any separator.
- So the output should be `1`, `2`, and `3` all together as `123`.

---

## Solution Code

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(i, end="")
```

---

## Code Explanation

- `n = int(input())`:  
  Reads an integer input from the user.

- `for i in range(1, n + 1)`:  
  Loops through all numbers from `1` to `n` (inclusive).

- `print(i, end="")`:  
  Prints each number `i` **without moving to the next line** and **without any spaces**.  
  - The `end=""` argument in the `print()` function tells Python to **keep printing on the same line** with no space or newline after each number.

**Important Note:**  
- You are **not** allowed to use any **string methods** like `.join()`, `.split()`, `.replace()`, etc.
- Only simple looping and `print()` with `end=""` are used.
