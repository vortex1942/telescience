# This script processes screenshots from the Map-world verb in SS13
# They can be processed into Full map images, and/or Goonhub Compatable images

# ***Suggested __build.dm configuration***
#   #define IM_REALLY_IN_A_FUCKING_HURRY_HERE 1 // Skips atmo build, Hides lobby & changelogs (Gotta go fast!)
#   #define I_AM_ABOVE_THE_LAW                  // Disables security bots (No doors being opened or moving bots)
#   #define ALL_ROBOT_AND_COMPUTERS_MUST_SHUT_THE_HELL_UP // Disables bots (No doors being opened or moving bots)
#   #define BAD_MONKEY_NO_BANANA                // Disables monkey spawns (No items getting thrown around)
#   #define NO_RANDOM_ROOMS                     // Disables random rooms on stations
# Don't forget to enable your map override

# ***Ingame STEPS***
# 1. Give yourself Godmode, and the XRAY mutation [Toggle-Your-Godmode, Manage-Bioeffects > Name > + > XRAY]
# 2. Place PDA and all items in backpack (Either hide your backpack in a locker or repeat Step4)
# 3. Del-all /atom/moveable/screen/hud
# 4. Right-click the Yellow stamina box > View Variables > Hard Delete
# 5. Game > Effects > Parallax # Lets us turn space purple
# 6. Run Map-World command (All defaults except for Z-Level)
# 7 Place screenshots into a folder dedicated for raw images (You should have 100 Images)
# 8 Create an output folder
# 9 Run the script and follow the prompts (Prompt Explanations below)

# Script Prompts
# RAW Image directory/           // Location of map screenshots,     (USE A SEPERATE FOLDER for each map, There should only be 100 images)
# PROCESSED Image Directory      // Location of all outputed files   (Files with matching names will be overwritten)
# RAW Image Renaming         [N] // Rename all .png files in the raw image folder (Optional)
# RAW Image Name             // New [name] for RAW images, Uses "[name]_[INT].png" format
# Export Full Image          [Y] // Export a full image of the map
# Export Image Name          // Name of the Full exported image  (E.g Cogmap1_full)
# Apply transparency         [Y] // Good for file opimisation,       (Enable make space pink when running Map-world, Hides background elements (E.g planets, SS12))
# Goonhub formatting         [N] // Splices the image into 1200x1200 segments and names them "X,Y.png" accordingly
#                            ^ Default values

# *****************************************************************
# ******ALL .pngs in the rawimages folder will be processed********
# ******Exported files may be overwritten/renamed in the output****
# *****************************************************************

from PIL import Image
from os import listdir, rename


def get_user_choice(prompt):
    choice = input(prompt).lower()
    if choice in ["y", "yes"]:
        return True
    else:
        return False


# Function for renming RAW images to [NAME]_[INT].png, E.g Cogmap1_22.png
def func_imagerenamer():
    x = 1
    imagelist = [
        file
        for file in (sorted(listdir(raw_img_dir), key=len))
        if file.endswith(".png")
    ]
    for file_name in imagelist:
        source = raw_img_dir + "\\" + file_name
        new = raw_img_dir + "\\" + f"{RAWfilename}_{x}.png"
        # Change new filename preset here ^^^^^^^^^^^
        rename(source, new)
        x += 1


# Function for applying transparency to all purple areas[254,0,232] Will take 30 secs to process
def func_transparancy():
    print("APPLYING TRANSPARANCY")
    data = master_export.getdata()
    transparancy_data = []
    for item in data:
        if item[0] == 255 and item[1] == 0 and item[2] == 228:
            transparancy_data.append((255, 255, 255, 0))
        else:
            transparancy_data.append(item)
    master_export.putdata(transparancy_data)
    print("TRANSPARENCY PASS COMPLETE")


# Function for saving the image (params: name=Filename, export=Image IMG variable)
def func_exportfullimage(name, export):
    print("SAVING IMAGE")
    file = img_dir + "\\" + name + ".png"
    print(file)
    file = open(file, "wb")
    export.save(file)


# Selection of Input/Output directories
raw_img_dir = str(input("Directory of RAW images: "))
img_dir = str(input("Directory for PROCESSED images:"))


rename_image = get_user_choice(
    "Rename ALL RAW .png files to '[name]_[INT].png' [Y/\033[1mN\033[0m]:"
)
if rename_image:
    RAWfilename = str(input("RAW image [name]: "))


export_full_image = get_user_choice("Save a full image? [Y/\033[1mN\033[0m]:")
if export_full_image:
    exportfilename = str(input("Filename for Full Image (E.g Cogmap1_full): "))

transparency = get_user_choice(
    "Make Pink areas transparent?(Slow) [Y/\033[1mN\033[0m]:"
)

goonhub_splice = get_user_choice(
    "Splice & Rename image into GoonHub formating? [Y/\033[1mN\033[0m]:"
)


# Where the magic happens, Creates a canvas and pastes RAWimages in a grid fashion

# Sometimes it warns sometimes it doesn't I dunno
print("DecompressionBombWarnings may occour due to image size")

master_export = Image.new("RGBA", (9600, 9600), color=(255, 255, 255, 255))
image_list = [
    file for file in sorted(listdir(raw_img_dir), key=len) if file.endswith(".png")
]
x = 0
y = 0
for index, image_path in enumerate(image_list):
    file = raw_img_dir + "\\" + str(image_path)
    image = Image.open(file).convert("RGBA")
    if x == 9600:
        x = 0
        y += 960

    print(
        f"POS: {x//960}:{y//960}",
        f"FILE: {image_path : >13}",
    )

    master_export.paste(image, (x, y))
    x += 960


# Function splices the large image into Goonhub Compatable images [1200x1200 w/ name=(x,y.png)]
def func_goonhubsplice():
    width = height = 960
    goon_row_size = 9
    for x in range(0, goon_row_size + 1):
        for y in range(0, goon_row_size + 1):
            box = (y * width, x * height, (y + 1) * width, (x + 1) * height)
            a = master_export.crop(box)
            func_exportfullimage(f"{y},{x}", a)  # Yes it's y before x, Blame GoonAPIv2


# Function calls according to previous user selections
if rename_image:
    # Shouldn't matter if ran before or after processing
    func_imagerenamer()

if transparency:
    func_transparancy()

if export_full_image:
    func_exportfullimage(exportfilename, master_export)

if goonhub_splice:
    func_goonhubsplice()


# Hopefully you got this far
print("COMPLETED :)")
