# 📝 Python String Mutation

## 🧾 Problem Statement

You are given a **string** and your task is to change the character at a specified index.
Since strings in Python are **immutable**, you cannot directly assign values to an index, so you need to work around this.

---

## 🔧 Function Description

### `mutate_string(string, position, character)`

* **Parameters:**

  * `string (str)`: The original string to be modified.
  * `position (int)`: The index at which the character should be changed.
  * `character (str)`: The new character to insert.

* **Returns:**

  * `string`: The modified string with the character replaced at the specified position.

---

## 🔢 Input Format

* **First line**: A string `s`.
* **Second line**: An integer `position`, followed by a single character `character` (space-separated).

---

## 📤 Output Format

* Print the modified string after replacing the character at the given position.

---

## 🧪 Sample Input

```
abracadabra
5 k
```

## ✅ Sample Output

```
abrackdabra
```

---

## 💡 Explanation

* The input string is `"abracadabra"`.
* You are asked to replace the character at index 5 (which is `'a'`) with `'k'`.
* The new string becomes `"abrackdabra"`.

### 🔍 Input Handling in Code:

```python
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
```

* `s = input()` takes the string.
* `i, c = input().split()` reads the position and character, and splits them into two variables.
* `mutate_string(s, int(i), c)` calls the function to replace the character at index `i` with `c`.

---

## ✅ Solution Code

```python
def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

---

## 🧠 Code Breakdown

* `lst = list(string)`           : Convert the string into a list
* `lst[position] = character`    : Modify the desired character
* `string = "".join(lst)`        : Join the list back into a string
