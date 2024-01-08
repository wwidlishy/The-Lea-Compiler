; Lea (Template Asm Generator, Please DO NOT MODIFY ANY OF THIS FILE)

; nasm -f win32 filename.asm -o filename
; gcc -m32 filename.o -o filename

section .text
    global _main

    ; Imports
    extern _printf

; Temp Strings

message: db "Hello, World!", 10, 0
end_message:

; Body
_main:
    push message
    call _printf

    ret