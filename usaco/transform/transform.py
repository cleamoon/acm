"""
ID: yj1
LANG: PYTHON3
TASK: transform
"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
fout.write (str(sum) + '\n')
fout.close()

