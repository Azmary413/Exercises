# Python Nested Lists Problem

## Problem Statement

Given the names and grades for each student in a class, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Important:**  
If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

---

## Input Format

- The first line contains an integer, `n`, the number of students.
- The next `n` pairs of lines each contain:
  - A student's name (string).
  - The student's grade (float).

## Constraints

- 2 ≤ n ≤ 5 × 10⁵  
- There will always be one or more students having the second lowest grade.

## Output Format

- Print the name(s) of the student(s) with the second lowest grade.
- If there are multiple students, print each name on a new line in **alphabetical order**.

---

## Sample Input 0
```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

## Sample Output 0
```
Berry
Harry
```

### Explanation:
- We collect all the students and their grades:
  ```
  [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
  ```
- The lowest grade is 37.2 (Tina).
- The second lowest grade is 37.21 (Harry and Berry).
- After sorting names alphabetically, we print:
  ```
  Berry
  Harry
  ```

---

## Solution Code

```python
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted({s for n, s in students})
    second_lowest = scores[1]

    names = [n for n, s in students if s == second_lowest]
    for name in sorted(names):
        print(name)
```

---

## Code Explanation

- `students = []`  
  Initialize an empty list to store student names and their grades.

- `for _ in range(int(input())):`  
  Read the number of students and iterate to collect their names and grades.

- `scores = sorted({s for n, s in students})`  
  Create a **unique set** of scores and sort them in ascending order.

- `second_lowest = scores[1]`  
  The second element in the sorted list is the second lowest grade.

- `names = [n for n, s in students if s == second_lowest]`  
  Extract the names of students who have the second lowest grade.

- `for name in sorted(names):`  
  Sort the selected names alphabetically and print each one on a new line.

---

**Important Note:**  
Always sort the names alphabetically if multiple students share the second lowest grade.
