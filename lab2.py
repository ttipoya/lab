#Шеснадцатиричные числа, у которых 3 справа цифры равна А16 расположенные в порядке убывания. Для каждой такой последовательности максимальное число вывести прописью.
import re
file = open("text.txt","r")
buf = 0
res = 0
maxi = "0"
ch = '0'
d = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
while True:
    buf = file.readline().split()
    if not buf:
        print("-------------------------")
        print("Числа закончились или файл пуст")
        break
    for j in buf:
        res = re.findall(r'[0-9 A-F]*[A][0-9 A-F]{2}',j)
        if len(res) == 1:
            if int(ch,16) < int(res[0],16):
                if int(maxi,16) < int(res[0],16):
                    maxi = res[0]
                ch = res[0]
                for n in range(len(maxi)):
                    for l in range(len(d)):
                        if str(l) == maxi[n]:
                            print(d[l], end=' ')
                            break
                        elif d[l] == maxi[n]:
                            print(d[l], end=' ')
                print("")
            elif int(ch,16) > int(res[0],16):
                ch = res[0]
                maxi = "0"
        elif len(res) == 0:
                maxi = "0"
