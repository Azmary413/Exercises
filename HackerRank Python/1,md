## 📌 Problem : String Validation

### 🔍 Problem Statement

You are given a string.
Your task is to check the presence of:

* Alphanumeric characters
* Alphabetical characters
* Digits
* Lowercase letters
* Uppercase letters

### 📥 Input Format

* A single line containing the string `s`

### 📤 Output Format

Print five lines of Boolean values (`True` or `False`) indicating the presence of:

1. Alphanumeric characters
2. Alphabetical characters
3. Digits
4. Lowercase characters
5. Uppercase characters

### ✅ Sample Input

```
qA2
```

### ✅ Sample Output

```
True
True
True
True
True
```

### 🧠 Solution

```python
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
```

---

### 🔍 Line-by-Line Breakdown:

- **`any(c.isalnum() for c in s)`**

   * Checks if **any character** in the string is alphanumeric (either a letter or a digit).
   * Returns `True` if **at least one** character passes `.isalnum()`.

- **`any(c.isalpha() for c in s)`**

   * Checks if the string has **any alphabetic** characters (only letters, a-z or A-Z).

- **`any(c.isdigit() for c in s)`**

   * Returns `True` if there's **any digit** in the string (0–9).

- **`any(c.islower() for c in s)`**

   * Returns `True` if the string contains **any lowercase** letter (a–z).

- **`any(c.isupper() for c in s)`**

   * Returns `True` if the string contains **any uppercase** letter (A–Z).
