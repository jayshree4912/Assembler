from sys import *
###Symboltable code###
def symtab(f):
    line=[]
    sym=[]
    define=[]
    undefine=[]
    size=[]
    value=[]
    stype=[]
    label=[]
    addl=[]
    undefine_label=['jmp','je','jl','jg','jge','jle']
    fn=open(f,"r")
    l1=fn.readline()
    sl=l1.split()
    ln=len(sl)
    add=00000000
    l=1
    while(l1!=""):
        for i in range(ln):
            if(sl[i]=='dd'):
                line.append(l)
                sym.append(sl[i-1])
                s=sl[i+1].split(",")
                sz=len(s)*4
                define.append('D')
                size.append(sz)
                value.append(sl[i+1])
                stype.append('int')
                addl.append(add)
                add+=sz
                
                
            if(sl[i]=='db'):
                line.append(l)
                sym.append(sl[i-1])
                vl=[]
                for j in range(i+1,ln):
                    if(sl[j]!='0'):
                        vl.append(sl[j])
                s2=",".join(vl)
                s3=s2.split(',')
                s4=[]
                for i in range(len(s3)):
                    if(s3[i]=='0'):
                        for j in range(i):
                            s4.append(s3[j])
                s5=','.join(s4)
                s6=s5.replace(","," ")
                s7=s6.replace('"','')

                sz=len(s7)
                value.append(s7)
                define.append('D')
                size.append(sz)
                stype.append('byte')
                addl.append(add)
                add=00000000
    
               
            if(sl[i]=='dw'):
                line.append(l)
                sym.append(sl[i-1])
                s=sl[i+1].split(",")
                sz=len(s)*2
                define.append('D')
                size.append(sz)
                value.append(sl[i+1])
                stype.append('word')
                addl.append(add)
                add+=sz
               
            if(sl[i]=='resb'):
                line.append(l)
                sym.append(sl[i-1])
                define.append('D')
                size.append(sl[i+1])
                value.append('-')
                stype.append("Reserved Byte")
                addl.append(add)
                s1=int(sl[i+1])
                add+=s1
               
            if(sl[i]=='resd'):
                line.append(l)
                sym.append(sl[i-1])
                define.append('D')
                size.append(sl[i+1])
                value.append('-')
                stype.append("Reserved integer")
                addl.append(add)
                s1=int(sl[i+1])
                add+=s1*4
               
            if(sl[i]=='global'):
                line.append(l)
                sym.append(sl[i+1])
                define.append('U')
                size.append('-')
                value.append('-')
                stype.append("Function")
                addl.append('')

            if(sl[i]=='extern'):
                line.append(l)
                sym.append(sl[i+1])
                define.append('D')
                size.append('-')
                value.append('-')
                stype.append("Function")
                addl.append('')

            if sl[i].endswith(":"):
                s=sl[i]
                s1=s[:-1]
                if s1 not in sym:
                    line.append(l)
                    sym.append(s1)
                    define.append('U')
                    size.append('-')
                    value.append('-')
                    stype.append("Label")
                    addl.append('')
                else:
                     exit
                
            if sl[i] in undefine_label:
                if sl[i+1] not in sym:
                    line.append(l)
                    sym.append(sl[i+1])
                    define.append('U')
                    size.append('-')
                    value.append('-')
                    stype.append("Label")
                    addl.append('')
                else:
                    exit
                              
        l1=fn.readline()
        sl=l1.split()
        ln=len(sl)
        l+=1   
    fw=open("symbol_tab.txt","w")
    cnt=1
    for i in range(len(sym)):
        fw.write(str(sym[i])+"\t"+str("sym")+str(cnt)+"\t"+str(addl[i]).zfill(8)+"\t"+str(value[i])+"\n")
        cnt+=1
    fw=open("symtab_output.txt","w")
    fw.write("LineNo"+"\t"+"Symbol"+"\t"+"D/U"+"\t"+"Size"+"\t"+"Type"+"\t\t\t"+"Value"+"\t\t\t"+"Address"+"\n")
    for i in range(len(line)):
        fw.write(str(line[i])+"\t"+str(sym[i])+"\t"+str(define[i])+"\t"+str(size[i])+"\t"+str(stype[i])+"\t\t\t"+str(value[i])+"\t\t\t"+str(addl[i]).zfill(8)+"\n")
