section .data
	a dd 5
	b dd 1
	c dd 10
	d dd 20
	ans db "addition is %f",10,0
	msg3 db "element in array1:",10,0
section .text
	global main
	extern printf
main:
	mov eax,a
	mov edx,b
	mov c,eax
	mov eax,ebx
	push a
	call printf
	mul eax,a
	div eax,ebx
	add eax,ebx
	sub ebx,b
	mov ecx,12
	mov eax,14
	mov edx,12
	mov eax,13
	mov eax,'a'
	mov al,'z'
	mov bl,'A'
	mov bx,23
