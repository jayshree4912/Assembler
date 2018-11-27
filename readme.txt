Input file:
 1.new_sample.asm
 2.opcode.txt
 3.mod_rm.txt
 4.op_register.txt

Output file:
1.symtab_output.txt
2.literal_output.txt
3.intermediate_output.txt
4.lstcode.txt
5.object_output.myobj

Following steps are use to Run Assembler Program:
Step1:-
      First run assembler code file using following command;=.
      -----python3 assembler.py new_sample.asm
Step2:-
      Run main.py file to show output.Following options are display
      1.Display Symbol table
      2.Display Literal table
      3.Display Intermediate Code
      4.Display lst-code file
      5.Display object code

Step3:-For display (Symbol Table)1st option run following command
      ------python3 main.py st

Step4:-For display(Literal Table) 2nd option run following command
      ------python3 main.py lt
      
Step5:-For display(InterMediate Code) 3rd option run following command
      ------python3 main.py ic

Step6:-For display(Lst Code) 4th option run following command
      ------python3 main.py lst

Step7:-For display (Object File)5th option run following command
      ------python3 main.py obj

