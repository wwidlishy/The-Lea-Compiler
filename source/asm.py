class Functions:
    template_func = lambda name, count, afc: \
f"""__LEA_FUNCTION_{name}_{count}:
FI_{afc}:
    ; Initializes the arguments into memory
FB_{afc}:
    ; Function Body
FE_{afc}:
    ; Returns to After Call
"""
    template_call = lambda name, count, fcc: \
f"""; Call '{name}'.v = {count}
FC_{fcc}:
    ; Save stack & Pass arguments
FCE_{fcc}:
    ; Load stack
"""
    def syscall(rax, rdi=None, rsi=None, rdx=None):
        r = '\n'
        return f"""\
mov rax, {rax}
{('mov rdi, ' + str(rdi)) if rdi != None else r}{('mov rsi, ' + str(rsi)) if rsi != None else r}{('mov rdx, '+ str(rdx)) if rdx != None else r}syscall
"""
class Variables:
    pass

def gen_asm(argv1, order):
    assembly = \
    f"; Generated with Lea\n\n; nasm -f elf64 {argv1}.s -o {argv1}.o\n; ld {argv1}.o -o {argv1}.exe\n\nbits 64\nglobal _start\njmp _start\n\n_start:\n"
    for line in order:
        for operation in line:
            if operation[0] == "call":
                if operation[1] == "exit":
                    tokens = operation[2]
                    if len(tokens) == 1:
                        if tokens[0][0] == "number":
                            assembly += Functions.syscall(60,tokens[0][1])
                            return assembly
    assembly += "\n\nmov rax, 60\nmov rdi, 0\nsyscall"
    return assembly

def gen_file(argv1, assembly):
    with open(f"{argv1}.s", "w") as writer:
        writer.write(assembly)