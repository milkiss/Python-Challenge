from PIL import Image
i = Image.open("oxygen.png")

pixels = i.load() # this is not a list, nor is it list()'able
i.convert('RGB')
width, height = i.size
x = 0

all_pixels = [0]
while x <= width:
  y = height/2
  cpixel = pixels[x, y]
  if cpixel[0] == cpixel[1] and cpixel[1] == cpixel[2]:
    all_pixels.append(cpixel[0])
  x = x + 7
        
print all_pixels