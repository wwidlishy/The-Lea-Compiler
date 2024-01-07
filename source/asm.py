class ASM:
    # 0 linux 1 windows
    template = \
[
"""global _start

section .text

_start:
###BODY###

  mov rax, 60  
  mov rdi, 0 
  syscall          
""",
"""    global _main
    extern  _GetStdHandle@4
    extern  _WriteFile@20
    extern  _ExitProcess@4

    section .text
_main:
    mov     ebp, esp
    sub     esp, 4

###BODY###

    push    0
    call    _ExitProcess@4

    hlt
"""
]
    build_process = \
[
    "nasm -f elf64 filename.asm -o filename.o && gcc filename.o -o filename",
    "nasm -f win32 filename.asm -o filename.o && gcc filename.o -o filename.exe"
]