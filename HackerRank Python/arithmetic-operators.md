# Python Arithmetic Operators Problem

## Problem Statement

Given two integers `a` and `b`, perform the following operations:

- Print the sum of `a` and `b`.
- Print the difference of `a` and `b` (calculated as `a - b`).
- Print the product of `a` and `b`.

---

## Input Format

- The first line contains the first integer, `a`.
- The second line contains the second integer, `b`.

## Constraints

- 1 ≤ a ≤ 10⁴
- 1 ≤ b ≤ 10⁴

## Output Format

- Print three lines:
  - The first line should contain the sum (`a + b`).
  - The second line should contain the difference (`a - b`).
  - The third line should contain the product (`a * b`).

---

## Sample Input 0
```
3
2
```

## Sample Output 0
```
5
1
6
```

### Explanation:
- **Sum**: 3 + 2 = 5
- **Difference**: 3 - 2 = 1
- **Product**: 3 × 2 = 6

Each result is printed on a new line in the given order.

---

## Solution Code

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)   # Sum
    print(a - b)   # Difference (a - b)
    print(a * b)   # Product
```

---

## Code Explanation

- `a = int(input())` and `b = int(input())`:  
  Reads two integer inputs from the user.

- `print(a + b)`:  
  Calculates and prints the sum of `a` and `b`.

- `print(a - b)`:  
  Calculates and prints the result of `a` minus `b`.

- `print(a * b)`:  
  Calculates and prints the product of `a` and `b`.

**Important Note:**  
Each result must be printed on a separate line in the order: sum, difference, product.
