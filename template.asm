; Generated with lea

section .text
@linux    global main
@windows    global _main

    ; Imports
@linux    extern printf
@windows    global _printf

@linux    jmp main
@windows    jmp _main

; Functions

$functions

; Temp Constants

$tempcontants

; Body
@linux:main:
$body

@linux:    mov eax, 1
@linux:    xor ebx, ebx
@linux:    int 0x80

    ret