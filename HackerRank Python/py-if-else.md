# Python If-Else Problem

## Problem Statement

Given an integer `n`, perform the following conditional actions:

- If `n` is **odd**, print **Weird**.
- If `n` is **even** and in the inclusive range of **2 to 5**, print **Not Weird**.
- If `n` is **even** and in the inclusive range of **6 to 20**, print **Weird**.
- If `n` is **even** and greater than **20**, print **Not Weird**.

---

## Input Format

- A single line containing a positive integer `n`.

## Constraints

- 1 ≤ n ≤ 100

## Output Format

- Print **Weird** if the number is considered weird.
- Print **Not Weird** otherwise.

---

## Sample Input 0
```
3
```

## Sample Output 0
```
Weird
```

### Explanation:
- 3 is odd. According to the rules, odd numbers are considered "Weird".

---

## Sample Input 1
```
24
```

## Sample Output 1
```
Not Weird
```

### Explanation:
- 24 is even and greater than 20, so it is "Not Weird".

---

## Solution Code

```python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
```

---

## Code Explanation

- `n = int(input().strip())`:  
  Reads an integer input from the user, removing any leading or trailing spaces.

- `if n % 2 == 1:`  
  Checks if the number is odd (remainder when divided by 2 is 1).  
  - If **True**, it prints **Weird**.

- `elif 2 <= n <= 5:`  
  Checks if `n` is even and falls between 2 and 5 (inclusive).
  - If **True**, it prints **Not Weird**.

- `elif 6 <= n <= 20:`  
  Checks if `n` is even and falls between 6 and 20 (inclusive).
  - If **True**, it prints **Weird**.

- `else:`  
  If none of the above conditions are satisfied (meaning `n` is even and greater than 20),
  - It prints **Not Weird**.

**Important Note:**  
The conditions are checked in order.  
- Odd numbers are caught first.
- Even numbers are then categorized into different ranges.

