n=int(input('Enter no. of rows for Pyramid:- '))
for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))