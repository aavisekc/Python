### **Right-Angled Triangle Pattern with Asterisks (*) - Explanation**  

A **right-angled triangle pattern** made of asterisks (`*`) is a common programming exercise where the output forms a right-angled shape with increasing stars in each row.  

#### **Key Features of the Pattern:**
1. **Structure:**  
   - The triangle has `n` rows (where `n` is given as input).  
   - The first row has **1 star**, the second has **2 stars**, and so on until the `n-th` row, which has `n` stars.  
   - The right angle is typically at the **bottom-left** (but variations exist).  

2. **Example (for `n = 5`):**  
   ```
   *
   **
   ***
   ****
   *****
   ```

#### **How to Build the Pattern?**
1. **Loop through rows:**  
   - Use a loop (like `for` or `while`) to iterate from `1` to `n`.  
   - Each iteration represents a new row.  

2. **Print stars in each row:**  
   - For the `i-th` row, print `i` stars.  
   - This can be done by:  
     - A nested loop that runs `i` times (printing one star each time).  
     - Or, using string multiplication (`"*" * i`).  

3. **Move to the next line after each row:**  
   - After printing stars for a row, move to a new line (`print()` in Python).  

#### **Variations of the Pattern:**
1. **Inverted Right-Angled Triangle (Right angle at top-left):**  
   ```
   *****
   ****
   ***
   **
   *
   ```
   - Achieved by looping from `n` down to `1`.  

2. **Right-Angled Triangle (Right angle at top-right):**  
   ```
       *
      **
     ***
    ****
   *****
   ```
   - Requires adding leading spaces before stars.  

