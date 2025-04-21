# Write a Python function to generate a hollow triangle pattern
def hollow_triangle(n):
    for i in range(1, n + 1):
        if i == 1:
            print(' ' * (n - i) + '*')
        elif i == n:
            print('*' * (2 * n - 1))
        else:
            print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')
