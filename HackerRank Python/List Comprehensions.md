# Python List Comprehensions Problem

## Problem Statement

Let's learn about **list comprehensions**!  
You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid, along with an integer `n`.  
You need to **print a list of all possible coordinates** `(i, j, k)` on a 3D grid where the sum `i + j + k` **is not equal to** `n`.  
Use **list comprehension** instead of multiple loops.

---

## Input Format

- Four integers `x`, `y`, `z`, and `n`, each provided on a separate line.

## Constraints

- 0 ≤ x, y, z ≤ 100
- 0 ≤ n ≤ x + y + z

## Output Format

- Print a list of all valid `[i, j, k]` lists, in **lexicographic increasing order**.

---

## Sample Input 0
```
1
1
1
2
```

## Sample Output 0
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Explanation:
- Variables `i`, `j`, and `k` can take values from `0` up to `x`, `y`, and `z` respectively.
- All possible lists `[i, j, k]` are generated.
- Lists where the sum `i + j + k == 2` are **excluded**.
- The resulting list is printed.

---

## Sample Input 1
```
2
2
2
2
```

## Sample Output 1
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 2]]
```

---

## Solution Code

```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k] 
              for i in range(x + 1) 
              for j in range(y + 1) 
              for k in range(z + 1) 
              if (i + j + k) != n]
    
    print(result)
```

---

## Code Explanation

- `x = int(input())`, `y = int(input())`, `z = int(input())`, `n = int(input())`:  
  Reads four integers from the user.

- `[[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]`:  
  - This **list comprehension** generates all possible `[i, j, k]` lists.
  - `i` goes from `0` to `x`, `j` goes from `0` to `y`, and `k` goes from `0` to `z`.
  - **Only** includes the coordinates where the sum `i + j + k` **is not** equal to `n`.

- `print(result)`:  
  Prints the final list in lexicographic order.

---

**Important Note:**  
- This method avoids using multiple nested loops.
- List comprehensions make the code **shorter, cleaner, and faster**.
