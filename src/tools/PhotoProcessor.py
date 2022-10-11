from select import select
from PIL import Image, ImageDraw
from os import walk, getcwd, path, listdir, rename

#rootdir = getcwd()
#imgdir = path.join(rootdir,"src","images","cogmap2")
#rawimgdir = path.join(imgdir, "rawimages")
#print(rootdir)
#print(imgdir)
#print(os.listdir(imgdir))


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


SELrenaming = str(input("Rename ALL RAW .png files to 'name_(X,Y).png' [y/" f"\033[1mN\033[0m]:"))
if SELrenaming.lower() == "y" or SELrenaming.lower() == "yes":
    RAWfilename = "test28"
    RAWfilename = str(input("RAW image name: "))
    func_imagerenamer()

SELexportfullimage = "yes"
#SELexportfullimage = input("Save a full image? [Y/" f"\033[1mn\033[0m]: ")
if SELexportfullimage.lower() == "n" or SELexportfullimage.lower() == "no":
    SELexportfullimage = False
else:
    exportfilename = "test28"
    #exportfilename = str(input("filename for Full Image: "))
    SELexportfullimage = True


SELtransparency = "no"
#SELtransparency = input("Make Pink areas transparent?(Slow) [Y/" f"\033[1mn\033[0m]: ")
if SELtransparency.lower() == "n" or SELtransparency.lower() == "no":
    SELtransparency = False
else:
    SELtransparency = True



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

def func_exportfullimage():
    print("SAVING FULL IMAGE")
    file = (imgdir+"\\"+exportfilename+".png")
    print(file)
    file = open(file, "wb")
    masterexport.save(file) 
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

    print("iter: " f"{fc : >2}", "IMG XY: " f"{x : >4}", f"{y : >4}", "FILE: " f"{imagelist[ic] : >13}"      )
    masterexport.paste(photo, (x, y))
    x+=960
    ic+=1
    fc+=1

if SELtransparency == True:
    func_transparancy()

if SELexportfullimage == True:
    func_exportfullimage()


