import os
import shutil
# this script will be used to nest items within folders of the same name
folder_path = str(input("input folder path"))

os.chdir(folder_path)
# iterate through each file within the folder
for root, dirs, files in os.walk('.'):
    for i in files:
        # for each file
        og_path = os.path.join(root, i) # original path
        # step 1 make dirs
        # this will strip the extension from the name
        # to create the new folder
        new_folder = os.path.splitext(og_path)[0]
        # create folder if it does not exist
        if not (os.path.exists(new_folder)):
            os.mkdir(new_folder)

        # move file into new folder
        shutil.move(og_path,new_folder)
        print(i, "successfully moved")
