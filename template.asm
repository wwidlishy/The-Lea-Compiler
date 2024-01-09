; Generated with lea

@linux ; nasm -f elf $.asm -o $.o;
@linux ; gcc -m32 $.o -o $;
@windows ; nasm -f win32 $.asm -o $.o;
@windows ; gcc -m32 $.o -o $.exe

section .text
@linux    global main
@windows    global _main

@linux    jmp main
@windows    jmp _main

; Functions

$functions

; Temp Constants

$tempcontants

; Body
@linux main:
@windows _main:
$body
    ret