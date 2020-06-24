from PIL import Image, ImageDraw, ImageFilter


file_name = input("provide a location to your file\n")
img = Image.open(file_name)
pixels = img.load()
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        print(pixels[i,j])
        if pixels[i,j] == (0, 0, 0,0):
            # change to black if found transparent pixel
            pixels[i,j] = (0, 0, 0,255)
        else:
            #change to white for now
            pixels[i,j] = (254,254,254,255)
img.show()