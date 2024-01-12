; Generated with Lea

; nasm -f elf64 ../examples/test.lea.s -o ../examples/test.lea.o
; ld ../examples/test.lea.o -o ../examples/test.lea.exe

bits 64
global _start
jmp _start

exit:
    fi_0:
        push rax
    fb_0:
        mov rax, 60
        syscall
    fe_0:
        pop rax
        jmp rsi

_start:

fc_0:
    push rdi
    push rsi

    mov rdi, 2
    mov rsi, fce_0
    jmp exit
fce_0:
    pop rdi
    pop rsi
