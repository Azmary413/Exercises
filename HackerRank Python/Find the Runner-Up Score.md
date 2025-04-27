# Python Runner-Up Score Problem

## Problem Statement

Given the participants' score sheet for your University Sports Day, you are required to find the **runner-up score**.  
You are given `n` scores. Store them in a list and find the score of the **runner-up** (the second highest score).

---

## Input Format

- The first line contains an integer `n`, the number of participants.
- The second line contains `n` space-separated integers, each representing a participant's score.

## Constraints

- 2 ≤ n ≤ 10⁵
- -100 ≤ score ≤ 100

## Output Format

- Print the **runner-up score**.

---

## Sample Input 0
```
5
2 3 6 6 5
```

## Sample Output 0
```
5
```

### Explanation:
- The given list is `[2, 3, 6, 6, 5]`.
- The maximum score is `6`.
- The second maximum (runner-up) score is `5`.
- Hence, we print `5` as the runner-up score.

---

## Solution Code

```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score = max(arr)
    
    filtered_arr = [score for score in arr if score != max_score]
    
    runner_up = max(filtered_arr)
    
    print(runner_up)
```

---

## Code Explanation

- `n = int(input())`:  
  Reads the number of scores (number of participants).

- `arr = list(map(int, input().split()))`:  
  Reads the participant scores and stores them in a list as integers.

- `max_score = max(arr)`:  
  Finds the maximum score in the list.

- `filtered_arr = [score for score in arr if score != max_score]`:  
  Creates a new list that excludes all scores equal to the maximum score.

- `runner_up = max(filtered_arr)`:  
  Finds the maximum score from the filtered list, which is the **runner-up score**.

- `print(runner_up)`:  
  Prints the runner-up score.

---

**Important Note:**  
If the highest score occurs multiple times, all of them should be ignored when finding the runner-up.
