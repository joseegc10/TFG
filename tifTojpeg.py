import os
from PIL import Image
#run this script with python3
# current_path is the path where you want to create the converted dataset (by default is the current path of the conversion script)
# source_path is the path where the original dataset is stored (by default is the current path of the conversion script)
source_path = '/Users/yassirben/Desktop/earthengine/coordinates/Mangrove'
current_path = os.getcwd()

#create the new converted dataset folder
newpath = current_path+'/Mangrove_jpg_converted_LOCATE_dataset' 
if not os.path.exists(newpath):
os.makedirs(newpath)

for root, dirs, files in os.walk(source_path, topdown=False):
for folder in dirs:
print(folder)
#create converted classes sub-folders
subfolder_path = newpath+'/'+folder 
if not os.path.exists(subfolder_path):
os.makedirs(subfolder_path)
original_image_path=source_path+'/'+folder
print(original_image_path)
for r, d, f in os.walk(original_image_path, topdown=False):
for i in f:
im = Image.open(original_image_path+'/'+i)
print("Converting into jpeg the image %s" % i)
im.thumbnail(im.size)
i = i.replace('.tif','.jpg')
im.save(''+subfolder_path+'/'+i, "JPEG", quality=100)