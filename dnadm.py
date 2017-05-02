#Author - Utkarsh
#RNo. - 20161073

import csv

def distance (str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    len3 = min(len1,len2)
    if len2 > len1:
        str = str1
        str1 = str2
        str2 = str
    i = 0
    mismatch = 0
    distance = 1
    while(True):
        str3 = str1[i:len3+i]
        for pos in range(0,len3):
            if str3[pos] != str2[pos]:
                mismatch +=1
        mdistance = mismatch*1.00/len3
        if mdistance < distance:
            distance = mdistance
        i += 1
        if i > len1 - len3:
            break
    return(round(distance,4))

in_file = open("Nucleotide.txt","r")
op_file = open("Ndistance.txt","w")
writer = csv.writer(op_file, delimiter = ",")
s1 = in_file.read()

l1 = s1.split(">")
l2=['*']
l3 = []
l1.pop(0)

for a in l1:
    a = a.title()
    l2.append(a[a.find("(")+1:a.find(")")])
writer.writerow(l2)

for i in l1:
        a = i.split("\r\n")
        a = list(filter(None, a))
        a.pop(0)
        seq = ''.join(a)
        l3.append(seq)

for i in range(len(l3)):
    str1 = l3[i]
    strtmp = []
    if i < len(l2):
        strtmp.append(l2[i+1])
    for j in range(len(l3)):
        str2 = l3[j]
        strtmp.append(distance(str1,str2))
    writer.writerow(strtmp)

in_file.close()
op_file.close()