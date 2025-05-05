
# 📝 Python Find a Substring

## 🧾 Problem Statement

You are given a **string** and a **substring**.  
Your task is to count the number of times the substring appears in the string, including **overlapping** occurrences.  
The comparison is **case-sensitive**.

---

## 🔧 Function Description

### `count_substring(string, sub_string)`

* **Parameters:**

  * `string (str)`: The original string.
  * `sub_string (str)`: The substring you want to find and count.

* **Returns:**

  * `int`: The total number of overlapping occurrences of `sub_string` in `string`.

---

## 🔢 Input Format

* **First line**: A string `string`.
* **Second line**: A string `sub_string`.

---

## 📤 Output Format

* An integer indicating the number of times the `sub_string` occurs in the `string`.

---

## 🧪 Sample Input

```
ABCDCDC
CDC
```

## ✅ Sample Output

```
2
```

---

## 💡 Explanation

* The input string is `"ABCDCDC"`.
* The substring `"CDC"` appears **twice**:
  * First at index 2–4
  * Second at index 4–6 (overlapping)
* So, the output is `2`.

### 🔍 Input Handling in Code:

```python
string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
```

* `string = input().strip()` reads the original string.
* `sub_string = input().strip()` reads the substring.
* `count_substring(...)` returns the number of occurrences.

---

## ✅ Solution Code

```python
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
```

---

## 🧠 Code Breakdown

* `range(len(string) - len(sub_string) + 1)`
  Ensures the loop runs up to the point where the remaining characters are enough to match `sub_string`.

* `string[i:i + len(sub_string)]`
  Slices the string to extract a substring of the same length as `sub_string`.

* `== sub_string`
  Compares each slice with the target substring.

* `count += 1`
  Increments the count if a match is found.
