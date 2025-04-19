rows=input("Enter the number of rows: ")
rows=int(rows)
for i in range(1, rows + 1):
    print("Row number is", i)
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line
# # Output:
# """   
# 1
# 1 2                       

