import glob
import shutil
import random
files=glob.glob("cownum/train/*.jpg")
print(files)
testidices=random.sample(range(0,len(files)), int(.1*len(files)))
for i in testidices:
    shutil.move(files[i],"cownum/val/")
    shutil.move(files[i].replace("jpg","txt"), "cownum/val/")


