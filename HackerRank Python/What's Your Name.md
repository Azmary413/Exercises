# 👋 Python Full Name Greeting

## 🧾 Problem Statement

You are given the **first name** and **last name** of a person as input on two separate lines.
Your task is to **print a personalized greeting** in the following format:

```
Hello firstname lastname! You just delved into python.
```

---

## 🔢 Input Format

* The **first line** contains a string: the person’s **first name**.
* The **second line** contains a string: the person’s **last name**.

---

## 📤 Output Format

* Print one line with the message:

```
Hello firstname lastname! You just delved into python.
```

Where `firstname` and `lastname` are replaced with the actual names.

---

## ✅ Constraints

* The length of both the first and last names will be **≤ 10** characters.
* Names contain only **alphabetic characters** (no digits or symbols).

---

## 🧪 Sample Input

```
Ross
Taylor
```

## ✅ Sample Output

```
Hello Ross Taylor! You just delved into python.
```

---

## 💡 Explanation

* The inputs are two separate strings: `"Ross"` and `"Taylor"`.
* These are combined with proper spacing and printed in the required message format.

---

## ✅ Solution Code

```python
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```

---

## 🧠 Code Breakdown

* `def print_full_name(first, last):`
  Defines a function that takes two arguments: `first` and `last`.

* `print(f"Hello {first} {last}!...")`
  Uses an f-string to format the message by embedding the names into the sentence.

* `input()`
  Reads input from the user on the command line.
