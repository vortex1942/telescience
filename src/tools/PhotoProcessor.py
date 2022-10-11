from select import select
from PIL import Image, ImageDraw
from os import walk, getcwd, path

#rootdir = getcwd()
#imgdir = path.join(rootdir,"src","images","cogmap2")
#rawimgdir = path.join(imgdir, "rawimages")
#print(rootdir)
#print(imgdir)
#print(os.listdir(imgdir))

rawimgdir = str(input("Root Directory of RAW images: "))
imgdir = str(input("Directory for PROCESSED images:"))



SELexportfullimage = input("Save a full image? [Y/" f"\033[1mn\033[0m]: ")
if SELexportfullimage.lower() == "n" or SELexportfullimage.lower() == "no":
    SELexportfullimage = False
else:
    filename = str(input("Export full image filename: "))
    SELexportfullimage = True

#SELtransparency = "no"
SELtransparency = input("Make Pink areas transparent?(Slow) [Y/" f"\033[1mn\033[0m]: ")
if SELtransparency.lower() == "n" or SELtransparency.lower() == "no":
    SELtransparency = False
else:
    SELtransparency = True


#input("PAUSE")
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

def func_exportfullimage(imgdir,filename):
    print("SAVING FULL IMAGE")
    file = (imgdir+"\\"+filename+".png")
    print(file)
    file = open(file, "wb")
    masterexport.save(file) 
    print("FILE SAVED")



print("DecompressionBombWarnings may occour due to image size")
masterexport = Image.new("RGBA", (9600,9600), color=(255,255,255,255))
lst = ["(16, 16, 1)","(46, 16, 1)","(76, 16, 1)","(106, 16, 1)","(136, 16, 1)","(166, 16, 1)","(196, 16, 1)","(226, 16, 1)","(256, 16, 1)","(286, 16, 1)","(16, 46, 1)","(46, 46, 1)","(76, 46, 1)","(106, 46, 1)","(136, 46, 1)","(166, 46, 1)","(196, 46, 1)","(226, 46, 1)","(256, 46, 1)","(286, 46, 1)","(16, 76, 1)","(46, 76, 1)","(76, 76, 1)","(106, 76, 1)","(136, 76, 1)","(166, 76, 1)","(196, 76, 1)","(226, 76, 1)","(256, 76, 1)","(286, 76, 1)","(16, 106, 1)","(46, 106, 1)","(76, 106, 1)","(106, 106, 1)","(136, 106, 1)","(166, 106, 1)","(196, 106, 1)","(226, 106, 1)","(256, 106, 1)","(286, 106, 1)","(16, 136, 1)","(46, 136, 1)","(76, 136, 1)","(106, 136, 1)","(136, 136, 1)","(166, 136, 1)","(196, 136, 1)","(226, 136, 1)","(256, 136, 1)","(286, 136, 1)","(16, 166, 1)","(46, 166, 1)","(76, 166, 1)","(106, 166, 1)","(136, 166, 1)","(166, 166, 1)","(196, 166, 1)","(226, 166, 1)","(256, 166, 1)","(286, 166, 1)","(16, 196, 1)","(46, 196, 1)","(76, 196, 1)","(106, 196, 1)","(136, 196, 1)","(166, 196, 1)","(196, 196, 1)","(226, 196, 1)","(256, 196, 1)","(286, 196, 1)","(16, 226, 1)","(46, 226, 1)","(76, 226, 1)","(106, 226, 1)","(136, 226, 1)","(166, 226, 1)","(196, 226, 1)","(226, 226, 1)","(256, 226, 1)","(286, 226, 1)","(16, 256, 1)","(46, 256, 1)","(76, 256, 1)","(106, 256, 1)","(136, 256, 1)","(166, 256, 1)","(196, 256, 1)","(226, 256, 1)","(256, 256, 1)","(286, 256, 1)","(16, 286, 1)","(46, 286, 1)","(76, 286, 1)","(106, 286, 1)","(136, 286, 1)","(166, 286, 1)","(196, 286, 1)","(226, 286, 1)","(256, 286, 1)","(286, 286, 1)",]
x = ic = fc = 0
per = 10
y = 8640
for p in lst:
    file = rawimgdir+"\\"+str(lst[ic])+".png"
    photo = Image.open(file).convert("RGBA") 
    if fc == 10:
        fc = x = 0
        y -= 960
        per += 10
        print(per,"%")
    #Verbose print
    #print("iter: " f"{fc : >2}", "IMG XY: " f"{x : >4}", f"{y : >4}", "FILE: " f"{lst[ic] : >13}"      )
    masterexport.paste(photo, (x, y))
    x+=960
    ic+=1
    fc+=1

if SELtransparency == True:
    func_transparancy()

if SELexportfullimage == True:
    func_exportfullimage(imgdir, filename)


