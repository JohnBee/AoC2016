import hashlib
import struct
hexChar = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
def check(byteStr):
    for i in byteStr:
        if ord(i)!=0:
            return False
    return True

def genCode(codeWord):
    code = ""
    i = 0
    while len(code) != 8:
        m = hashlib.md5()
        m.update(codeWord+str(i))
        dig = m.digest()
        if check(dig[:2]) and ord(dig[2])<16:
            let = hexChar[ord(dig[2])]
            code += let
            print let, [ord(a) for a in dig]
        i+=1
    return code
print genCode("abc")
