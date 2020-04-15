# link resource: https://github.com/Rasmusb94/imageCropper/blob/master/run.py

# Image test
import os

# sys didn't be used
# import sys

from PIL import Image
count = 1
weather = ["Sunny", "Rain", "Cloudy", "Snow", "Fog"]
# labels of weather
weather_labels = ['Sunny', 'Rain', 'Cloudy', 'Snow', 'Fog']

# Change directory of pictures to crop
directory = "cloudytrain"
path = "Image2Weather/" + directory

# default the dir path
dir_name = 'data/'

# read the images of different directories
for roots, dirs, files in os.walk(dir_name, topdown=True):
    if (len(dirs) != 0):
        for index in range(0, len(dirs)):
            print(dirs[index])

    '''
    print(roots)
    print(len(files))
    '''

print('done')

# directory of weather condition images

'''
for infile in os.listdir(path):
    if infile.endswith('.jpg'):
        print(infile)
        i = Image.open(os.path.join(path, infile))
        print(i.format, i.size)
        if i.height < 300:
            box = box = (0, 0, i.width, i.height)
        else:
            box = (0, 0, i.width, 300)
        region = i.crop(box)
        fn, fext = os.path.splitext(infile)

        # Change weather
        region.save('{}/Cropped/{}_{}{}'.format(path, count, weather[2], fext))

        count += 1
if count > 1:
    print("Cropped " + str(count - 1) + " images to the " + path + " directory.")
else:
    print("No images were cropped.")
'''
