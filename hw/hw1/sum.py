import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('hitchens.cs.colorado.edu',1234))

listt = []
data = s.recv(1024)
data += s.recv(1024)

for i in range(0, 14, 4):
   listt.append(struct.unpack('<I', data[i:i+4])[0])

s.send( struct.pack('<Q', (sum(listt))))
print "revceived: "
print s.recv(1024)
