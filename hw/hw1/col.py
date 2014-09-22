import socket
import struct
import md5
import bisect

l = []

for n in range(0, 100000000):
    m = md5.new(str(n))
    temp = m.hexdigest()
    temp2 = temp[0:6]
    temp3 = temp[26:32]
    temp4 = temp2+temp3
    i = bisect.bisect_left(l, temp4)
    if i != len(l) and l[i] == temp4:
        print "success on iteration " + str(n)
        print "it looks like " + str(temp4)
        break
    else:
        l.insert(i, temp4)
    if not (n%100000):
        print str(n) + " iterations done"
