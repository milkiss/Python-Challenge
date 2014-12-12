data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

l = []
for c in data:
  if ('a' <= c and c <= 'z'):
    nc = ord(c)+2
    k = ord('z')-ord('a')+1
    l.append(chr((nc-ord('a'))%k+ord('a')))
  else:
    l.append(c)

print "".join(l)