from PIL import Image
import ImageGrab
import os
import numpy as np

bbox = (714,149,721,156)
sample  = "C:/Users/vssharma/Pictures/Screenshots/Screenshot (30).png" 
bg = Image.open(sample)
sampletag = bg.crop(bbox)
temp = np.array(sampletag)
tagarraypixel = temp[:,:,:3]

testArea = ()     #pixel values to be cropped 
while True:
    current  = ImageGrab.grab()
    filename = os.getcwd()+'\\image.png'        #save filename 
    current.save(filename, 'PNG')
    fg = Image.open(filename)                   ##foreground
    currentTag  = fg.crop(bbox)
    currentarraypixel = np.array(currentTag)

    if np.sum(tagarraypixel - currentarraypixel) == 0:
        target = current.crop(testArea)          #another bounding box which crops the image part needed(the test result on top of the stack)
        
    


