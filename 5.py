import pickle

res = pickle.load(open("banner.p", "rb"))

for l in res:
  print "".join([t[0]*t[1] for t in l])