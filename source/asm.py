class ASM:
    def template(argv):
        result = ""
        for i in open("template.asm", "r").read().split("\n"):
            if len(i) == 0:
                result += "\n"
                continue
            if i[0:len(f"@{argv[2]}")] == f"@{argv[2]}":
                result += i[len(f"@{argv[2]}")+1:] + "\n"
                continue
            if i[0] == "@":
                continue
            else:
                result += i + "\n"
        return result
    
class GASM:
    def __init__(self, argv) -> None:
        self.asm = ASM.template(argv)
        self.body = ""
    def generate(self, order) -> str:
        for line in order:
            for token in line:
                pass #orgazm

print(GASM([0, 0, "windows"]).asm)