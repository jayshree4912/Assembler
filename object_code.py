from sys import *
###Object Code###
def replace_x(s):
    for i in s:
        if(i=='x'):
            s=s.replace(i,'0')
    return s

def cal_add(s):
    cn=0
    ls=['[',']','(',')']
    for i in s:
        if i not in ls:
            cn+=1
        else:
            exit
        c=int(cn)/2
    return int(c)
def add_space(s):
    s1=[s[i:i+2] for i in range(0,len(s),2)]
    r=' '.join(s1)
    return r

def obj_code(f1,f2,f3,f4,f5,f6):
    arr=["eax","ebx","ecx","edx","ebp","esp","esi","edi"]
    arr1=["ax","bx","cx","dx"]
    arr2=["ah","al","bh","bl","ch","cl","dh","dl"]
    fn1=open(f1,"r")
    fn2=open(f2,"r")
    fn3=open(f3,"r")
    fn4=open(f4,"r")
    fn5=open(f5,"r")
    fn6=open(f6,"r")
    ln1=fn1.readline()
    ln2=fn2.read()
    ln3=fn3.read()
    ln4=fn4.read()
    ln5=fn5.read()
    ln6=fn6.read()

    ls1=ln1.split()
    ls2=ln2.split()
    ls3=ln3.split()
    ls4=ln4.split()
    ls5=ln5.split()
    ls6=ln6.split()

    l1=len(ls1)
    l2=len(ls2)
    l3=len(ls3)
    l4=len(ls4)
    l5=len(ls5)
    l6=len(ls6)
    fw=open("object_output.myobj","w")
    ls7=[]
    
    cnt=0
    while(ln1!=""):
        cnt+=1
        for i in range(l1):
            if(ls1[i]=="section"):
                if(ls1[i+1]==".data"):
                    add1=80840314
                    fw.write(str(add1)+"<__data_start>:"+"\n")
                if(ls1[i+1]==".bss"):
                    add2=80840200
                    fw.write(str(add2)+"<__bss_start>:"+"\n")        
            if(ls1[i]=="dd"):
                for j in range(l2):
                    if ls1[i-1]==ls2[j]:
                        a=ls2[j+3]
                oc=str(replace_x(hex(int(ls1[i+1])))).zfill(4)
                ls7.append(ls1[i-1])
                ls7.append(add1)
                fw.write("\t\t\t"+str(add1)+"\t"+str(add_space(oc))+"\n")
                add1=add1+int(a)
            if(ls1[i]=="db"):
                oc=str(replace_x(hex(10)+hex(0))).zfill(4)
                fw.write("\t\t\t"+str(add1)+"\t"+str(add_space(oc))+"\n")
            if(ls1[i]=="resb"):
                c=0000
                oc=str(c).zfill(4)
                a=ls1[i+1]
                fw.write("\t\t\t"+str(add2)+"\t"+str(add_space(oc))+"\n")
                add2=add2+int(a)
            if(ls1[i]=="resd"):
                c=0000
                oc=str(c).zfill(4)
                a=int(ls1[i+1])*4
                fw.write("\t\t\t"+str(add2)+"\t"+str(add_space(oc))+"\n")
                add2=add2+int(a)
            if(ls1[i]=="main:"):
                add=80840440
                fw.write(str(add)+"<main>:"+"\n")
            if(ls1[i]=="mov"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in ls2):
                    for j in range(len(ls7)):
                        if ls[1]==ls7[j]:
                            s1=ls7[j+1]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+str(s1)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in ls2):
                    for j in range(len(ls7)):
                        if ls[1]==ls7[j]:
                            s1=ls7[j+1]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+str(s1)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in ls2):
                    for j in range(len(ls7)):
                        if ls[1]==ls7[j]:
                            s1=ls7[j+1]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+str(s1)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr and ls[1] in arr):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in arr1):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in arr2):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=="add"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr and ls[1] in arr):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in arr1):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in arr2):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)

            if(ls1[i]=="sub"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in ls3):
                    for j in range(l3):
                        if ls[1]==ls3[j]:
                            s1=ls3[j]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1.zfill(8)[::-1]
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr and ls[1] in arr):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in arr1):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in arr2):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=="jmp"):
                for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="mul"):
                for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1+'E3'
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="div"):
                for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1+'F3'
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=='inc'):
                if(ls1[i+1] in arr):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls1[i+1] in arr1):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj='66'+p1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls1[i+1] in arr2):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+'C0'
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=='dec'):
                if(ls1[i+1] in arr):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls1[i+1] in arr1):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj='66'+p1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls1[i+1] in arr2):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+'C8'
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)

            if(ls1[i]=="xor"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in arr):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in arr1):
                    for x in arr1:
                        if x==ls[0]:
                            r1=x
                    for y in arr1:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in arr2):
                    for x in arr2:
                        if x==ls[0]:
                            r1=x
                    for y in arr2:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)

            if(ls1[i]=="cmp"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in arr):
                    for x in arr:
                        if x==ls[0]:
                            r1=x
                    for y in arr:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr1 and ls[1] in arr1):
                    for x in arr1:
                        if x==ls[0]:
                            r1=x
                    for y in arr1:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in arr2 and ls[1] in arr2):
                    for x in arr2:
                        if x==ls[0]:
                            r1=x
                    for y in arr2:
                        if y==ls[1]:
                            r2=y
                    for k in range(l4):
                        if ls4[k]==r1:
                            if ls4[k+1]==r2:
                                s1=ls4[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls[0] in (arr or arr1 or arr2) and ls[1].isdigit()):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+ls[1].zfill(2)
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=="je"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jz"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jne"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jg"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jge"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jl"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="jle"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="push"):
                if(ls1[i+1] in arr):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
                if(ls1[i+1] in ls2):
                    for k in range(l2):
                        if ls2[k]==ls1[i+1]:
                            s1=ls2[k+2]
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+s1
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=="call"):
                if(ls1[i+1]=="printf"):
                    for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                    for l in range(l6):
                        if str(p)==ls6[l]:
                            p1=ls6[l+1]
                    obj=p1+str(0).zfill(8)
                    fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                    add=add+cal_add(obj)
            if(ls1[i]=="std"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="cld"):
                for k in range(l5):
                        if str(cnt) == ls5[k]:
                            p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="ret"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
            if(ls1[i]=="loop"):
                for k in range(l5):
                    if str(cnt) == ls5[k]:
                        p=ls5[k+2]
                for l in range(l6):
                    if str(p)==ls6[l]:
                        p1=ls6[l+1]
                obj=p1
                fw.write("\t\t\t"+str(add).zfill(8)+"\t"+str(add_space(obj))+"\n")
                add=add+cal_add(obj)
    
        ln1=fn1.readline()
        ls1=ln1.split()
        l1=len(ls1)
