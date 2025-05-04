# 🔁 Python Swap Case Problem

## 🧾 Problem Statement

You are given a string and your task is to **swap the case** of each character in the string:

* All **lowercase letters** should be converted to **uppercase**
* All **uppercase letters** should be converted to **lowercase**

Characters that are **not letters** (like digits, symbols, punctuation) remain **unchanged**.

---

## 🔢 Input Format

* A single line containing a string `s`.

---

## ✅ Constraints

* `0 < len(s) ≤ 1000`
* The string can contain letters, digits, spaces, and punctuation.

---

## 📤 Output Format

* Print a single line: the string after swapping the case of each character.

---

## 🧪 Sample Input 0

```
HackerRank.com presents "Pythonist 2".
```

## ✅ Sample Output 0

```
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```

---

## 💡 Explanation

* Each lowercase letter becomes uppercase, and vice versa.
* `"H"` becomes `"h"`, `"a"` becomes `"A"`, and so on.
* The quotation marks (`"`) and number (`2`) remain unchanged.

---

## ✅ Solution Code

```python
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```

---

## 🧠 Code Breakdown

* `def swap_case(s):`
  Defines a function that takes a string `s` as input.

* `return s.swapcase()`
  Uses Python’s built-in `str.swapcase()` method to swap uppercase to lowercase and vice versa.

* `if __name__ == '__main__':`
  Ensures the code inside runs only if the file is executed as a script.

* `s = input()`
  Takes a string input from the user.

* `print(result)`
  Prints the swapped-case version of the input string.
