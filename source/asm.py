class Functions:
    pass
class Variables:
    pass

def gen_asm(order):
    for line in order:
        for operation in line:
            print(operation)