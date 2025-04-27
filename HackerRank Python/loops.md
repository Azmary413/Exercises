# Python Loops Problem

## Problem Statement

The provided code stub reads an integer `n` from standard input.

For all non-negative integers `i` less than `n`, print the square of `i` (that is, `i × i`), each on a new line.

---

## Input Format

- A single line containing the integer `n`.

## Constraints

- 1 ≤ n ≤ 20

## Output Format

- Print `n` lines.
- Each line contains the square of the corresponding non-negative integer `i` (where `i` ranges from `0` to `n-1`).

---

## Sample Input 0
```
5
```

## Sample Output 0
```
0
1
4
9
16
```

### Explanation:
- The list of non-negative integers less than 5 is: `[0, 1, 2, 3, 4]`.
- Their squares are: `0²=0`, `1²=1`, `2²=4`, `3²=9`, `4²=16`.

Each value is printed on a separate line.

---

## Solution Code

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
```

---

## Code Explanation

- `n = int(input())`:  
  Reads an integer input from the user.

- `for i in range(n)`:  
  Loops through all integers starting from `0` up to but **not including** `n`.

- `print(i * i)`:  
  For each `i`, it prints the result of `i` multiplied by itself (i.e., the square of `i`).

**Important Note:**  
The `range(n)` function generates numbers from `0` to `n-1`, which matches the required non-negative integers less than `n`.
