# Python Division Problem

## Problem Statement

The provided code stub reads two integers, `a` and `b`, from standard input.

Add logic to print two lines:
- The first line should contain the result of **integer division** `a // b`.
- The second line should contain the result of **float division** `a / b`.

**Note:**  
No rounding or formatting of the results is required.

---

## Input Format

- The first line contains the first integer, `a`.
- The second line contains the second integer, `b`.

## Constraints

- 1 ≤ a ≤ 10⁴
- 1 ≤ b ≤ 10⁴

## Output Format

- Print two lines:
  - First line: result of integer division (`a // b`).
  - Second line: result of float division (`a / b`).

---

## Sample Input 0
```
4
3
```

## Sample Output 0
```
1
1.3333333333333333
```

### Explanation:
- **Integer Division**: 4 // 3 = 1 (quotient without the remainder)
- **Float Division**: 4 / 3 = 1.3333333333333333

The integer division result is printed first, followed by the float division result.

---

## Solution Code

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)   # Integer Division
    print(a / b)    # Float Division
```

---

## Code Explanation

- `a = int(input())` and `b = int(input())`:  
  Reads two integer inputs from the user.

- `print(a // b)`:  
  Performs **integer division**, which discards any fractional part and only keeps the whole number result.

- `print(a / b)`:  
  Performs **float division**, which results in a decimal value.

**Important Note:**  
- Integer division (`//`) always returns an integer.
- Float division (`/`) always returns a float, even if the result looks like a whole number.
