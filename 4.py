import urllib, re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

n = 8022


while(True):
  response = urllib.urlopen(url % n)
  p = re.search(r"and the next nothing is (\w+)", response.read())
  if p == None:
    print response.read()
    break
  n = p.group(1)
  print n