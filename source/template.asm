; Generated with lea

; nasm -f elf64 $.asm -o $.o
; ld $.o -o $

bits 64

section .text

global _start
jmp _start

##TempValues##

##Functions##

_start:

##Body##

mov rax, 60
mov rdi, 0
syscall

ret