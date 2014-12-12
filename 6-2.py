import zipfile

zf = zipfile.ZipFile("channel/channel.zip")
print zf.getinfo("46145.txt").comment
