#! python3
#  identifyPhotoFolders.py - Prints folder paths where the majority of files are .png or .jpg

import os
from PIL import Image, UnidentifiedImageError

root = os.path.expanduser("~")

for foldername, subfolders, filenames in os.walk(root):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue
        try:
            im = Image.open(os.path.join(foldername,filename))
            width, height = im.size
        except UnidentifiedImageError:
            print('Could not open %s. Skipping to next file.\n' % filename)
            continue

        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles > numNonPhotoFiles:
        print('Photo folder found at:\n%s\n' % os.path.abspath(foldername))
