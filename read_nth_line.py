f = open("C:\\data\\HR_ovdim\\HR_ovdim_20200218_230047.xls","r",encoding="UTF-8")
for i, line in enumerate(f):
    # Note that i == n-1 for the nth line.
    if i == 1523689:
        #print hex
        #print(":".join("{:02x}".format(ord(c)) for c in line))
        print(line)
        break