Hollow Triangle Python Program Requirements

To create a Python program that prints a hollow triangle, here are the key requirements:

## Input Requirements:
- The program should accept an integer `n` representing the height of the triangle
- Optionally, it could accept a character/symbol to use for drawing the triangle (defaulting to `*` if not specified)

## Output Requirements:
- Print a hollow right-angled triangle with:
  - First row: 1 character
  - Last row: `n` characters
  - First and last character of each row should be printed
  - Only the first and last rows are completely filled
  - For other rows, only the first and last positions should contain the character, with spaces in between

## Example Output (n=5):
```
*
**
* *
*  *
*****
```

## Functional Requirements:
1. Handle edge cases (n=0, n=1)
2. Validate input to ensure it's a positive integer
3. Properly space the hollow parts of the triangle
4. Option to customize the drawing character

## Suggested Implementation Approach:
1. Use nested loops - outer for rows, inner for columns
2. For each row, determine if it's the first, last, or middle row
3. For middle rows, print character only at start and end positions
4. Include proper newline characters after each row

