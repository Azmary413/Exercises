# Python List Operations Problem

## 🧮 Problem Statement

You are given a series of commands to perform on an initially empty list. Each command modifies the list in some way, such as inserting, appending, or removing elements. Your task is to iterate through each command in order and perform the corresponding operation.

Whenever the command is `print`, output the current state of the list.

---

## 🔢 Input Format

- The first line contains an integer `N`, the number of commands.
- Each of the next `N` lines contains a command of one of the following types:
  - `insert i e`: Insert integer `e` at position `i`.
  - `print`: Print the list.
  - `remove e`: Delete the first occurrence of integer `e`.
  - `append e`: Append integer `e` to the list.
  - `sort`: Sort the list.
  - `pop`: Pop the last element.
  - `reverse`: Reverse the list.

---

## ✅ Constraints

- The elements to be added must be integers.
- All commands are guaranteed to be valid and in the correct format.

---

## 📤 Output Format

- For every `print` command, print the list on a new line.

---

## 🧪 Sample Input 0

```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

## ✅ Sample Output 0

```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

---

## 💡 Explanation

1. Insert `5` at index `0`: list becomes `[5]`
2. Insert `10` at index `1`: list becomes `[5, 10]`
3. Insert `6` at index `0`: list becomes `[6, 5, 10]`
4. `print`: output `[6, 5, 10]`
5. Remove `6`: list becomes `[5, 10]`
6. Append `9`: list becomes `[5, 10, 9]`
7. Append `1`: list becomes `[5, 10, 9, 1]`
8. Sort: list becomes `[1, 5, 9, 10]`
9. `print`: output `[1, 5, 9, 10]`
10. Pop: list becomes `[1, 5, 9]`
11. Reverse: list becomes `[9, 5, 1]`
12. `print`: output `[9, 5, 1]`

---

## ✅ Solution Code

```python
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(command[1]))
        elif cmd == "append":
            lst.append(int(command[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
```

---

## 🧠 Code Breakdown

- `N = int(input())`  
  Reads the number of commands to process.

- `lst = []`  
  Initializes an empty list.

- `command = input().split()`  
  Splits each input command into parts for parsing.

- `if-elif` blocks  
  Check for the command type and execute the respective list method.
