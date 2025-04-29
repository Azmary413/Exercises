# Python Student Average Score Problem

## 🧮 Problem Statement

You are given the names and marks of several students in a class. Store them in a dictionary with the student's name as the key and a list of their marks as the value.  
You are then given a student's name for whom you need to calculate and print the average marks, **rounded to two decimal places**.

---

## 🔢 Input Format

- The first line contains an integer `n`, the number of students' records.
- The next `n` lines each contain:
  - A student's name, followed by space-separated marks (integers or floats).
- The final line contains a single string: `query_name`, the name of the student to query.

---

## ✅ Constraints

- 2 ≤ n ≤ 10⁴  
- 0 ≤ marks ≤ 100  
- There will always be at least one valid student with marks.

---

## 📤 Output Format

- Print one line: the average of the marks obtained by the queried student, **formatted to 2 decimal places**.

---

## 🧪 Sample Input 0

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

## ✅ Sample Output 0

```
56.00
```

---

## 🧪 Sample Input 1

```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```

## ✅ Sample Output 1

```
26.50
```

---

## 💡 Explanation

- The `student_marks` dictionary is populated with names as keys and a list of scores as values.
- For the query student (e.g., Malika), we calculate the average using `sum(scores)/len(scores)`.
- The result is printed with **exactly two digits after the decimal point**, using Python string formatting.

---

## ✅ Solution Code

```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
```

---

## 🧠 Code Breakdown

- `name, *line = input().split()`  
  Splits the first word as the student’s name and the rest as scores.

- `map(float, line)`  
  Converts the score strings into float values.

- `student_marks[name] = scores`  
  Adds the entry to the dictionary.

- `f"{average:.2f}"`  
  Formats the average to exactly two decimal places.
