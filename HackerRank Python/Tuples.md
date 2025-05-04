# 🧮 Python Tuple Hash Problem

## 🧾 Problem Statement

You are given an integer `n` and `n` space-separated integers. Your task is to:

1. Create a tuple of those `n` integers.
2. Compute and print the result of `hash(tuple)`.

Python’s built-in `hash()` function can be used directly on immutable data types like tuples to produce a hash value.

---

## 🔢 Input Format

* The **first line** contains an integer `n`, the number of elements in the tuple.
* The **second line** contains `n` space-separated integers, which will form the tuple.

---

## ✅ Constraints

* 1 ≤ n ≤ 20
* Each element is an integer within the range −100 ≤ element ≤ 100

---

## 📤 Output Format

* Output a single integer — the hash value of the tuple.

---

## 🧪 Sample Input 0

```
2
1 2
```

## ✅ Sample Output 0

```
3713081631934410656
```

---

## 💡 Explanation

* First, `n = 2`, so we expect 2 integers.
* The second line is: `1 2`
* These are converted into a tuple: `(1, 2)`
* The built-in `hash()` function is applied to this tuple:
  ➡️ `hash((1, 2))`
* The result is the hash value of the tuple, which may vary by platform or Python version.

---

## ✅ Solution Code

```python
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
```

---

## 🧠 Code Breakdown

* `if __name__ == '__main__':`
  Ensures this script runs only when executed directly.

* `n = int(input())`
  Reads the number of elements to be placed in the tuple.

* `integer_list = map(int, input().split())`
  Reads a line of space-separated integers and converts them to an iterable of `int`.

* `t = tuple(integer_list)`
  Converts the iterable into a tuple.

* `print(hash(t))`
  Prints the hash value of the tuple using Python's built-in `hash()` function.
