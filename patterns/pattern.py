"""Simple Programing Langauge"""

print('Normal Pyramid')
print('Enter the number of rows')
n = int(input())
for i in range(n):
    x = '*'
    x = x*i
    print(f'{x:^10}')
