from select import select
from PIL import Image, ImageDraw
from os import listdir, rename, path
#1. Give yourself Godmode, and XRAY mutation
#2. Place PDA and all items in backpack
#3. Del-all /atom/moveable/screen/hud
#4. Manually edit "visibility" of stamina bar by right clicking and Viewing Variables" (Repeat with backpack or dump in locker)
#5. Run Map-World verb
#    All defaults except for Z-Level, only choose 1 for station
#Place screenshots in a dedicated folder and run script


rawimgdir = "S:\\telescience\\src\\images\\cogmap1\\rawimages"
#rawimgdir = str(input("Root Directory of RAW images: "))


imgdir = "S:\\telescience\\src\\images\\cogmap1"
#imgdir = str(input("Directory for PROCESSED images:"))


def func_imagerenamer():
    x = y = 1
    imagelist = [file for file in (sorted(listdir(rawimgdir), key=len)) if file.endswith('.png')]
    for file_name in imagelist:
        source = rawimgdir +"\\"+ file_name
        new = rawimgdir +"\\"+ f"{RAWfilename}_{x}.png"
        # Change new filename preset here ^^^^^^^^^^^ 
        rename(source, new)
        x+=1


SELrenaming = "no"
#SELrenaming = str(input("Rename ALL RAW .png files to 'name_INT.png' [y/" f"\033[1mN\033[0m]:"))
if SELrenaming.lower() == "y" or SELrenaming.lower() == "yes":
    RAWfilename = str(input("RAW image name: "))
    func_imagerenamer()


SELexportfullimage = "no"
#SELexportfullimage = input("Save a full image? [Y/" f"\033[1mn\033[0m]: ")
if SELexportfullimage.lower() == "n" or SELexportfullimage.lower() == "no":
    SELexportfullimage = False
else:
    exportfilename = "test28"
    #exportfilename = str(input("filename for Full Image: "))
    SELexportfullimage = True


SELtransparency = "yes"
#SELtransparency = input("Make Pink areas transparent?(Slow) [Y/" f"\033[1mn\033[0m]:")
if SELtransparency.lower() == "n" or SELtransparency.lower() == "no":
    SELtransparency = False
else:
    SELtransparency = True

SELgoonhubsplice = "Yes"
#SELgoonhubsplice = input("Resize&Splice image into GoonHub formating? [y/" f"\033[1mN\033[0m]:")
if SELgoonhubsplice.lower() == "y" or SELgoonhubsplice.lower() == "yes":
    SELgoonhubsplice = True

def func_transparancy():
    print("TRANSPARENCY PASS")
    data = masterexport.getdata()
    transparantdata = []
    for item in data:
        if item[0] == 254 and item[1] == 0 and item[2] == 232:
            transparantdata.append((255, 255, 255, 0))
        else:
            transparantdata.append(item)
    masterexport.putdata(transparantdata)
    print("TRANSPARENCY PASS COMPLETE")

def func_exportfullimage(name, export):
    print("SAVING IMAGE")
    file = (imgdir+"\\"+name+".png")
    print(file)
    file = open(file, "wb")
    export.save(file) 
    print("FILE SAVED")


print("DecompressionBombWarnings may occour due to image size")
masterexport = Image.new("RGBA", (9600,9600), color=(255,255,255,255))
imagelist = [file for file in sorted(listdir(rawimgdir), key=len) if file.endswith('.png')]
x = ic = fc = 0
per = 10
y = 8640
for p in imagelist:
    file = rawimgdir+"\\"+str(imagelist[ic])
    photo = Image.open(file).convert("RGBA") 
    if fc == 10:
        fc = x = 0
        y -= 960
        per += 10
        print(per,"%")
    #Verbose print
    #print("iter: " f"{fc : >2}", "IMG XY: " f"{x : >4}", f"{y : >4}", "FILE: " f"{imagelist[ic] : >13}")
    masterexport.paste(photo, (x, y))
    x+=960
    ic+=1
    fc+=1


def func_goonhubsplice(input, xPieces, yPieces):
    height = 9600 // yPieces
    width = 9600 // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = masterexport.crop(box)
            func_exportfullimage(f"{i},{j}", a)


if SELtransparency == True:
    func_transparancy()

if SELexportfullimage == True:
    func_exportfullimage(exportfilename, masterexport)

if SELgoonhubsplice == True:
    func_goonhubsplice(file, 8, 8)
