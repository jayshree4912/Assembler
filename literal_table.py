from sys import *
###Literal table code###
def lit(f):
    line_no=[]
    literal=[]
    hex_lit=[]
    fn=open(f,"r+")
    l1=fn.readline()
    sl=l1.split()
    ln=len(sl)
    cnt=1
    while(l1!=""):
        for i in range(ln):
            if(sl[i]=='mov'):
                s=sl[i+1].split(",")
                for j in range(len(s)):
                    if(s[j].isdigit()):
                        literal.append(s[j])
                        line_no.append(cnt)
                       
            if(sl[i]=='add'):
                s=sl[i+1].split(",")
                for j in range(len(s)):
                    if(s[j].isdigit()):
                        literal.append(s[j])
                        line_no.append(cnt)
                       
        l1=fn.readline()
        sl=l1.split()
        ln=len(sl)
        cnt+=1   
    fw=open("literal_output.txt","w")
    fw.write("LitNo"+"\t"+"Line"+"\t"+"Literal  "+"\t"+"HexLiteral"+"\n")
    p=1
    for i in range(len(literal)):
        fw.write(str(p)+"\t"+str(line_no[i])+"\t"+str(literal[i])+"\t\t"+str(hex(int(literal[i])))+"\n")
        p+=1

    fw=open("literal_table.txt","w")
    for i in range(len(literal)):
        fw.write(str(literal[i])+"\t"+"lit#"+str(literal[i])+"\n")
