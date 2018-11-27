from sys import *
from symbol_table import*
from literal_table import*
from intermmediate_table import*            
from lstfile_code import*
from object_code import*


if __name__=="__main__":
    f=argv[1]
    symtab(f)   
    lit(f)    
    transform(f,"symbol_tab.txt","literal_table.txt","op_register.txt")
    lst_code(f,"symbol_tab.txt","literal_table.txt","mod_rm.txt","intermediate_output.txt","opcode.txt")
    obj_code(f,"symbol_tab.txt","literal_table.txt","mod_rm.txt","intermediate_output.txt","opcode.txt")
