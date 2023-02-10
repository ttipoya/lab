a = []
c = []
n = 0
m = 0
l = 0
maxi = 0
o = 0
d = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
with open("text.txt") as f:
    for i in f.readline():
        a.append(i)
b = a[::-1]
b.count('a')
n = b.count('a')
for i in range(len(b)-(n*2)):
    if b[i] == 'a' and b[i+1] != 'a':
        b[i] = b[i] + b[i+1] + b[i+2]
        b[i] = b[i][::-1]
        b.pop(i+1); b.pop(i+1)
a = b[::-1]
for i in range(len(a)):
    if len(a[i]) == 1:
        if i != 0:
            a[i] = a[i - 1] + a[i]
            a[i-1] = ''
for i in range(len(a)):
    if len(a[i]) >= 3:
        c.append(a[i])
for i in range(len(c)-1):
    if int(c[i],16) > int(c[i+1],16)and m == 0:
        print("Одно из макс чисел:",c[i])
        t = c[i]
        print('Ввиде строк:', end=' ')
        for j in range(len(t)):
            for m in range(len(d)):
                if str(m) == t[j]:
                    print(d[m],end=' ')
                    break
                elif d[m] == t[j]:
                    print(d[m],end=' ')
        l += 1
        m += 1
    elif c[i] < c[i+1]:
        m == 0
if l == 0:
    print("Последовательности не найдено")