; Generated with Lea

; nasm -f elf64 ../examples/test.lea.s -o ../examples/test.lea.o
; ld ../examples/test.lea.o -o ../examples/test.lea.exe

bits 64
global _start
jmp _start

_start:
mov rax, 60
mov rdi, 0

syscall
