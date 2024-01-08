; Lea (Template Asm Generator, Please DO NOT MODIFY ANY OF THIS FILE)

; nasm -f elf filename.asm -o filename.o
; gcc -m32 filename.o -o filename

section .text
    global main

    ; Imports
    extern printf

; Temp Strings

message: db "Hello, World!", 10, 0
end_message:

; Body
main:
    push message
    call printf

    mov eax, 1
    xor ebx, ebx
    int 0x80

    ret