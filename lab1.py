file = open("text.txt",'r')
maxi = '0'
ch = ''
ch1 = '0'
ch2 = '0'
col = 0
d = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
buf = file.read(1)
if not buf:
        print("Файл пуст или нет нужных чисел")
while buf:
    if buf != " ":
        ch = ch + buf
        buf = file.read(1)
    else:
        if ch1 == '0':
            ch1 = ch
            continue
        else:
            ch2 = ch
        if int(ch1,16) > int(ch2,16) and ch1[2] == "A" and ch2[2] == "A":
            if int(maxi,16) < int(ch1,16) and col ==0:
                maxi = ch1
                for j in range(len(maxi)):
                    for l in range(len(d)):
                        if str(l) == maxi[j]:
                            print(d[l], end=' ')
                            break
                        elif d[l] == maxi[j]:
                            print(d[l], end=' ')
                print('')
            if col == 0:
                col +=1
            ch1 = ch2
        elif int(ch1,16) < int(ch2,16):
            ch1 = ch2
            col = 0
            maxi = "0"
        ch = ''
        buf = file.read(1)
