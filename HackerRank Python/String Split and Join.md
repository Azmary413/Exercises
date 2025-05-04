# 🔗 Python Split and Join Problem

## 🧾 Problem Statement

You are given a string consisting of **space-separated words**. Your task is to:

1. **Split** the string into a list of words using the space `" "` as a delimiter.
2. **Join** the words back together using a **hyphen `-`** as the separator.

---

## 🔢 Input Format

* A single line containing a string of **space-separated words**.

---

## 📤 Output Format

* A single string with **hyphen-separated words**.

---

## ✅ Constraints

* `0 < len(line) ≤ 1000`
* The string contains only **alphabetic characters and spaces**.

---

## 🧪 Sample Input

```
this is a string
```

## ✅ Sample Output

```
this-is-a-string
```

---

## 💡 Explanation

* The input string is split into: `["this", "is", "a", "string"]`
* Then it is joined back using hyphens: `"this-is-a-string"`

---

## ✅ Solution Code

```python
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```

---

## 🧠 Code Breakdown

* `line.split()`
  Splits the string wherever there is a space `" "`, and returns a list of words.

* `"-".join(...)`
  Joins the list of words into a single string using `-` as the separator.

* `input()`
  Takes user input from the command line.

* `print(result)`
  Prints the final hyphen-joined string.
