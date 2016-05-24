import os
import golly as g

x,y=0,0
w=110
h=7*8
bits = ""
dump = ""

for row in xrange(y, y+h):
   for col in xrange(x, x+w):
      if g.getcell(col, row) > 0:
         bits += "1"
         dump += "%d,%d\n" % (col, row)
      else:
         bits += "0"

g.setclipstr(dump+"r\n")

data = ""
i = 0
while len(bits) >= 8:
    v = int(bits[:8],2)
    bits = bits[8:]
    if 12 < (i % 0x6e) and i > 0x10 and i != 0x6d:
        v = 0xf4
    data += chr(v)
    i += 1

open("/tmp/life.bin","w").write(data)
os.system("objdump -M intel -b binary -m i386 -D /tmp/life.bin | grep -v hlt > /tmp/life.txt")
