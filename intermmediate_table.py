from sys import *
###Intermediate code###
def transform(f1,f2,f3,f4):
    arr=["eax","ebx","ecx","edx","ebp","esp","esi","edi"]
    arr1=["ax","bx","cx","dx"]
    arr2=["ah","al","bh","bl","ch","cl","dh","dl"]
    address=00000000
    fl1=open(f1,"r")
    fl2=open(f2,"r")
    fl3=open(f3,"r")
    fl4=open(f4,"r")
    ln1=fl1.readline()
    ln2=fl2.read()
    ln3=fl3.read()
    ln4=fl4.read()
    
    ls1=ln1.split()
    ls2=ln2.split()
    ls3=ln3.split()
    ls4=ln4.split()

    l1=len(ls1)
    l2=len(ls2)
    l3=len(ls3)
    l4=len(ls4)
    fw=open("intermediate_output.txt","w")
    cnt=0
    fw.write("--------------------Intermediate Code---------------------\n\n")
    while(ln1!=""):
        cnt+=1
        for i in range(l1):
            if (ls1[i]=="mov"):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in ls2):
                    op="op01"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            r=ls4[k+1]
                    for j in range(l2):
                        if ls2[j]==ls[1]:
                                n=ls2[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                elif(ls[0] in arr1 and ls[1] in ls2):
                    op="op02"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            r=ls4[k+1]
                    for j in range(l2):
                        if ls2[j]==ls[1]:
                                n=ls2[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                else:                            
                    if(ls[0] in arr2 and ls[1] in ls2):
                        op="op03"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                r=ls4[k+1]
                        for j in range(l2):
                            if ls2[j]==ls[1]:
                                n=ls2[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                        address+=6
                if(ls[0] in ls2 and ls[1] in arr): 
                    op="op04"
                    for k in range(l2):
                        if ls2[k]==ls[0]:
                            r=ls2[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                elif(ls[0] in ls2 and ls[1] in arr1):
                    op="op05"
                    for k in range(l2):
                        if ls2[k]==ls[0]:
                            r=ls2[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                else:
                    if(ls[0] in ls2 and ls[1] in arr2):
                        op="op06"
                        for k in range(l2):
                            if ls2[k]==ls[0]:
                                r=ls2[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                        address+=6
                if( ls[0] in arr and ls[1] in ls3):
                    op="op07"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                elif( ls[0] in arr1 and ls[1] in ls3):
                    op="op08"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                else:
                    if( ls[0] in arr2 and ls[1] in ls3):
                        op="op09"
                        for j in range(l4):
                            if ls4[j]==ls[0]:
                                r=ls4[j+1]
                        for k in range(l3):
                            if ls3[k]==ls[1]:
                                n=ls3[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                        address+=6
                if(ls[0] in arr and ls[1] in arr): 
                    op="op10"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                elif(ls[0] in arr1 and ls[1] in arr1):
                    op="op11"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                else:
                    if(ls[0] in arr2 and ls[1] in arr2):
                        op="op12"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                n1=ls4[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n2=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                        address+=3

            if (ls1[i]=="add"):
                ls=ls1[i+1].split(",")
                if( ls[0] in arr and ls[1] in ls3):
                    op="op13"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                elif( ls[0] in arr1 and ls[1] in ls3):
                    op="op14"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                else:
                    if( ls[0] in arr2 and ls[1] in ls3):
                        op="op15"
                        for j in range(l4):
                            if ls4[j]==ls[0]:
                                r=ls4[j+1]
                        for k in range(l3):
                            if ls3[k]==ls[1]:
                                n=ls3[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                        address+=6
                if(ls[0] in arr and ls[1] in arr):
                    op="op16"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                elif(ls[0] in arr1 and ls[1] in arr1):
                    op="op17"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                else:
                    if(ls[0] in arr2 and ls[1] in arr2): 
                        op="op18"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                n1=ls4[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n2=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                        address+=3
            if (ls1[i]=="sub"):
                ls=ls1[i+1].split(",")
                if( ls[0] in arr and ls[1] in ls3):
                    op="op19"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                elif( ls[0] in arr1 and ls[1] in ls3):
                    op="op20"
                    for j in range(l4):
                        if ls4[j]==ls[0]:
                            r=ls4[j+1]
                    for k in range(l3):
                        if ls3[k]==ls[1]:
                            n=ls3[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                    address+=6
                else:
                    if( ls[0] in arr2 and ls[1] in ls3): 
                        op="op21"
                        for j in range(l4):
                            if ls4[j]==ls[0]:
                                r=ls4[j+1]
                        for k in range(l3):
                            if ls3[k]==ls[1]:
                                n=ls3[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(r)+" "+str(n)+"\n")
                        address+=6
                if(ls[0] in arr and ls[1] in arr):
                    op="op22"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                elif(ls[0] in arr1 and ls[1] in arr1):
                    op="op23"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                else:
                    if(ls[0] in arr2 and ls[1] in arr2):
                        op="op24"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                n1=ls4[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n2=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                        address+=3
            if(ls1[i]=="jmp"):
                op="op25"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]
                        
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="mul"):
                if(ls1[i+1] in arr):
                    op="op26"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op27"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op28"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
            if(ls1[i]=="div"):
                if(ls1[i+1] in arr):
                    op="op29"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op30"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op31"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
            if(ls1[i]=="inc"):
                if(ls1[i+1] in arr):
                    op="op32"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op33"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op34"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
                if(ls1[i+1] in ls2):
                    op="op35"
                    for k in range(l2):
                        if ls2[k]==ls1[i+1]:
                            n=ls2[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
            if(ls1[i]=="dec"):
                if(ls1[i+1] in arr):
                    op="op36"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op37"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op38"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
                if(ls1[i+1] in ls2):
                    op="op39"
                    for k in range(l2):
                        if ls2[k]==ls1[i+1]:
                            n=ls2[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
            if(ls1[i]=="call"):
                op="op40"
                for k in range(l2):
                    if ls2[k]==ls1[i+1]:
                        n=ls2[k+1]
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="push"):
                if(ls1[i+1] in arr):
                    op="op41"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op42"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op43"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
                if(ls1[i+1] in ls2):
                    op="op44"
                    for k in range(l2):
                        if ls2[k]==ls1[i+1]:
                            n=ls2[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
            if(ls1[i]=="pop"):
                if(ls1[i+1] in arr):
                    op="op45"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                elif(ls1[i+1] in arr1):
                    op="op46"
                    for k in range(l4):
                        if ls4[k]==ls1[i+1]:
                            n=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                    address+=2
                else:
                    if(ls1[i+1] in arr2):
                        op="op47"
                        for k in range(l4):
                            if ls4[k]==ls1[i+1]:
                                n=ls4[k+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                        address+=2
            if(ls1[i]=='xor'):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in arr):
                    op="op48"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                elif(ls[0] in arr1 and ls[1] in arr1):
                    op="op49"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                else:
                    if(ls[0] in arr2 and ls[1] in arr2):
                        op="op50"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                n1=ls4[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n2=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                        address+=3
            if(ls1[i]=='cmp'):
                ls=ls1[i+1].split(",")
                if(ls[0] in arr and ls[1] in arr):
                    op="op51"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                elif(ls[0] in arr1 and ls[1] in arr1):
                    op="op52"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    for j in range(l4):
                        if ls4[j]==ls[1]:
                            n2=ls4[j+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                    address+=3
                else:
                    if(ls[0] in arr2 and ls[1] in arr2):
                        op="op53"
                        for k in range(l4):
                            if ls4[k]==ls[0]:
                                n1=ls4[k+1]
                        for j in range(l4):
                            if ls4[j]==ls[1]:
                                n2=ls4[j+1]
                        fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+str(n2)+"\n")
                        address+=3
                if(ls[0] in arr and ls[1].isdigit()): 
                    op="op54"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+" " +"\n")
                    address+=3
                if(ls[0] in arr1 and ls[1].isdigit()):
                    op="op55"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+" "+"\n")
                    address+=3
                if(ls[0] in arr2 and ls[1].isdigit()): 
                    op="op56"
                    for k in range(l4):
                        if ls4[k]==ls[0]:
                            n1=ls4[k+1]
                    fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n1)+" "+" "+"\n")
                    address+=3
            if(ls1[i]=="je"):
                op="op57"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jz"):
                op="op58"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jne"):
                op="op59"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]       
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jg"):
                op="op60"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]      
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jge"):
                op="op61"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]      
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jl"):
                op="op62"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]     
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="jle"):
                op="op63"
                for k in range(l2):
                    if ls1[i+1]==ls2[k]:
                        n=ls2[k+1]
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
            if(ls1[i]=="cld"):
                op="op64"
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+"\n")
                address+=2
            if(ls1[i]=="std"):
                op="op65"
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+"\n")
                address+=2
            if(ls1[i]=="ret"):
                op="op66"
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+"\n")
                address+=2
            if(ls1[i]=='loop'):
                op="op67"
                for k in range(l2):
                    if ls2[k]==ls1[i+1]:
                        n=ls2[k+1]
                fw.write(str(cnt)+"\t"+str(address).zfill(8)+"\t"+str(op)+" "+str(n)+" "+" "+"\n")
                address+=2
        ln1=fl1.readline()
        ls1=ln1.split()
        l1=len(ls1)
def replace_x(s):
    for i in s:
        if(i=='x'):
            s=s.replace(i,'0')
    return s.upper()
def cal_add(s):
    cn=0
    ls=['[',']','(',')']
    for i in s:
        if i not in ls:
            cn+=1
        else:
            exit
        c=cn/2
    return c
