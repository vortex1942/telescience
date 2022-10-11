#This script processes screenshots from the Map-world verb in SS13
#They can be processed into Full map images, and/or Goonhub Compatable images

# ***Suggested __build.dm configuration***
#   #define IM_REALLY_IN_A_FUCKING_HURRY_HERE 1 // Skips atmo build, Hides lobby & changelogs (Gotta go fast!)
#   #define I_AM_ABOVE_THE_LAW                  // Disables security bots (No doors being opened or moving bots)
#   #define ALL_ROBOT_AND_COMPUTERS_MUST_SHUT_THE_HELL_UP // Disables bots (No doors being opened or moving bots)
#   #define BAD_MONKEY_NO_BANANA                // Disables monkey spawns (No items getting thrown around)
#   #define NO_RANDOM_ROOMS                     // Disables random rooms on stations
# Don't forget to enable your map override

# ***Ingame STEPS***
#1. Give yourself Godmode, and the XRAY mutation [Toggle-Your-Godmode, Manage-Bioeffects > Name > + > XRAY]
#2. Place PDA and all items in backpack (Either hide your backpack in a locker or repeat Step4)
#3. Del-all /atom/moveable/screen/hud
#4. Right-click the Yellow stamina box > View Variables > Edit [visibility] = 0
#5. Run Map-World command (All defaults except for Z-Level)
#6 Place screenshots into a folder dedicated for raw images (You should have 100 Images)
#7 Create an output folder
#8 Run the script and follow the prompts (Prompt Explanations below)

# Script Prompts
#RAW Image directory/           // Location of map screenshots,     (USE A SEPERATE FOLDER for each map, There should only be 100 images)
#PROCESSED Image Directory      // Location of all outputed files   (Files with matching names will be overwritten)
#RAW Image Renaming         [N] // Rename all .png files in the raw image folder (Optional)
    #RAW Image Name             // New [name] for RAW images, Uses "[name]_[INT].png" format
#Export Full Image          [Y] // Export a full image of the map
    #Export Image Name          // Name of the Full exported image  (E.g Cogmap1_full)
#Apply transparency         [Y] // Good for file opimisation,       (Enable make space pink when running Map-world, Hides background elements (E.g planets, SS12))
#Goonhub formatting         [N] // Splices the image into 1200x1200 segments and names them "X,Y.png" accordingly
#                            ^ Default values

#*****************************************************************
#******ALL .pngs in the rawimages folder will be processed********
#******Exported files may be overwritten/renamed in the output****
#*****************************************************************

from select import select
from PIL import Image, ImageDraw
from os import listdir, rename, path

# Selection of Input/Output directories
rawimgdir = str(input("Directory of RAW images: "))
imgdir = str(input("Directory for PROCESSED images:"))


# Selection for RAWimage renaming
SELimagerenamer = str(input("Rename ALL RAW .png files to '[name]_[INT].png' [y/" f"\033[1mN\033[0m]:"))
if SELimagerenamer.lower() == "y" or SELimagerenamer.lower() == "yes":
    RAWfilename = str(input("RAW image [name]: "))
    SELimagerenamer = True


# Selection for exporting a full size image
SELexportfullimage = input("Save a full image? [Y/" f"\033[1mn\033[0m]: ")
if SELexportfullimage.lower() == "n" or SELexportfullimage.lower() == "no":
    SELexportfullimage = False
else:
    exportfilename = str(input("Filename for Full Image (E.g Cogmap1_full): "))
    SELexportfullimage = True


#Selection for applying transparency to purple areas (GoonhubSplices will be purple without this)
SELtransparency = input("Make Pink areas transparent?(Slow) [Y/" f"\033[1mn\033[0m]:")
if SELtransparency.lower() == "n" or SELtransparency.lower() == "no":
    SELtransparency = False
else:
    SELtransparency = True


# Splice/Rename the image into Goonhub compatable images
SELgoonhubsplice = input("Splice & Rename image into GoonHub formating? [y/" f"\033[1mN\033[0m]:")
if SELgoonhubsplice.lower() == "y" or SELgoonhubsplice.lower() == "yes":
    SELgoonhubsplice = True


# Function for renming RAW images to [NAME]_[INT].png, E.g Cogmap1_22.png
def func_imagerenamer():
    x = y = 1
    imagelist = [file for file in (sorted(listdir(rawimgdir), key=len)) if file.endswith('.png')]
    for file_name in imagelist:
        source = rawimgdir +"\\"+ file_name
        new = rawimgdir +"\\"+ f"{RAWfilename}_{x}.png"
        # Change new filename preset here ^^^^^^^^^^^ 
        rename(source, new)
        x+=1


# Function for applying transparency to all purple areas[254,0,232] Will take 30 secs to process
def func_transparancy():
    print("APPLYING TRANSPARANCY")
    data = masterexport.getdata()
    transparantdata = []
    for item in data:
        if item[0] == 254 and item[1] == 0 and item[2] == 232:
            transparantdata.append((255, 255, 255, 0))
        else:
            transparantdata.append(item)
    masterexport.putdata(transparantdata)
    print("TRANSPARENCY PASS COMPLETE")


# Function for saving the image (params: name=Filename, export=Image IMG variable)
def func_exportfullimage(name, export):
    print("SAVING IMAGE")
    file = (imgdir+"\\"+name+".png")
    print(file)
    file = open(file, "wb")
    export.save(file) 


#Sometimes it warns sometimes it doesn't I dunno
print("DecompressionBombWarnings may occour due to image size")


# Where the magic happens, Creates a canvas and pastes RAWimages in a grid fashion
masterexport = Image.new("RGBA", (9600,9600), color=(255,255,255,255))
imagelist = [file for file in sorted(listdir(rawimgdir), key=len) if file.endswith('.png')]
x = ic = fc = 0
per = 10
y = 8640
# For loop stitches RAw images together
for p in imagelist:
    file = rawimgdir+"\\"+str(imagelist[ic])
    photo = Image.open(file).convert("RGBA") 
    if fc == 10:
        fc = x = 0
        y -= 960
        per += 10
        print(per,"%")
    #Verbose mode [Iteration]   [Image Coords]  [RAW Filename]
    #print("iter: " f"{fc : >2}", "IMG XY: " f"{x : >4}", f"{y : >4}", "FILE: " f"{imagelist[ic] : >13}")
    masterexport.paste(photo, (x, y))
    x+=960
    ic+=1
    fc+=1


#Function splices the large image into Goonhub Compatable images [1200x1200 w/ name=(x,y.png)]
def func_goonhubsplice():
    height = 9600 // 8
    width = 9600 // 8
    for i in range(0, 8):
        for j in range(0, 8):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = masterexport.crop(box)
            func_exportfullimage(f"{i},{j}", a)


#Function calls according to previous user selections
if SELimagerenamer == True:
    #Shouldn't matter if ran before or after processing
    func_imagerenamer()

if SELtransparency == True:
    func_transparancy()

if SELexportfullimage == True:
    func_exportfullimage(exportfilename, masterexport)

if SELgoonhubsplice == True:
    func_goonhubsplice()


# Hopefully you got this far
print("COMPLETED :)")