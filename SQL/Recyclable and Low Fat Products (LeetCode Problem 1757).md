# Recyclable and Low Fat Products (LeetCode Problem 1757)

## Problem Description
The `Products` table contains information about products, including whether they are low fat and recyclable. The table structure is as follows:

- **product_id**: An integer that uniquely identifies a product (Primary Key).
- **low_fats**: An ENUM (`'Y'` or `'N'`) that indicates whether the product is low fat (`'Y'` for yes, `'N'` for no).
- **recyclable**: An ENUM (`'Y'` or `'N'`) that indicates whether the product is recyclable (`'Y'` for yes, `'N'` for no).

### Objective
Write a SQL query to find the product IDs of products that are **both low fat and recyclable**.

### Example Input and Output
**Input Table:**
```
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
```

**Output:**
```
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
```

### Explanation
Only products with `low_fats = 'Y'` and `recyclable = 'Y'` are selected. In the given input, products with IDs 1 and 3 meet the criteria.

---

## SQL Solution

Here is the SQL query to solve the problem:

```sql
SELECT product_id
FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

### Explanation of the Query
1. **`SELECT product_id`**: Extracts only the `product_id` column from the `products` table.
2. **`FROM products`**: Specifies the table to query.
3. **`WHERE low_fats = 'Y' AND recyclable = 'Y'`**:
   - Filters rows where the `low_fats` column has a value of `'Y'`.
   - Filters rows where the `recyclable` column has a value of `'Y'`.
   - Combines both conditions using the `AND` operator to ensure that only products meeting both criteria are included.

---

## Notes
- The query assumes the ENUM values are case-sensitive and use single quotes for strings.
- The result can be returned in any order, as no specific sorting is required.

---

## Example Run
Given the sample `Products` table:
```
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
```

Executing the query will yield:
```
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
```

This matches the expected output.