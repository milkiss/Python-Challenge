import re, zipfile

n = 90052
filename = "channel/%s.txt"
zf = zipfile.ZipFile("channel/channel.zip")
c = []

while(True):
  f = open(filename%n, "rb")
  data = f.read()
  f.close()
  res = re.search(r"Next nothing is (\w+)", data)
  if res == None:
    print data
    break
  n = res.group(1)
  c.append(zf.getinfo(n+".txt").comment)
  
print "".join(c)