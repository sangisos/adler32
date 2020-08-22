import sys
import os

def adler32(string):
    MOD = 65521
    a,b = 1,0
    for c in string:
        a = (a + ord(c)) % MOD
        b = (b+a) % MOD
    return format((b << 16) + a,'X')

if __name__ == "__main__" :
    if len(sys.argv) < 3 or not (sys.argv[1] == "-s" or sys.argv[1] == "-f"):
        print("Usage:\n\t",
              sys.argv[0],"-s <string>\n\t",
              sys.argv[0],"-f <file>\n")
        sys.exit(0)
    if sys.argv[1] == "-f":
        if os.access(sys.argv[2], os.R_OK):
            with open(sys.argv[2]) as fp:
                print(adler32(fp.read()))
                sys.exit(0)
        else:
            print("Can't read file", sys.argv[2])
            sys.exit(1)
    elif sys.argv[1] == "-s":
        print(adler32(sys.argv[2]))
        sys.exit(0)

