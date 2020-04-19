'''
This program compares all images in a folder to the weather prediction model
and sorts them accordingly in a new directory
'''
#imports
from imageai.Prediction.Custom import CustomImagePrediction
import os
import os.path
import datetime
from datetime import date
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#Array of weather conditions
weathers = ['sunny', 'rain', 'cloudy', 'snow']
#Path to the folder holding the images to test
path = "sampletest/testdata"
#Date for naming the directory
today = date.today()
date = today.strftime("%d-%m-%Y")
#String for creating a new directory
savePath = path + "/" + str(date)
#Create a new directory unless it already exists
try:
    os.mkdir(savePath)
    print("Directory ", savePath, " created.")
    #Loop array of weathers and create new directories in the main folder
    for weather in weathers:
        createDir = savePath + "/" + weather
        os.mkdir(createDir)
except FileExistsError:
    print("Directory ", savePath, " already exists.")

#Font for drawing on the image
font = ImageFont.truetype("arial.ttf", 26)
#Set path for execution
execution_path = os.getcwd()
#predict the image using the model class and trained weather model
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("sampletest/model_ex-110_acc-0.722222.h5")
prediction.setJsonPath("sampletest/model_class.json")
prediction.loadModel(num_objects=10)

#loop the items in the selected directory
for infile in os.listdir(path):
    #loop only jpg, jpeg and png files
    if infile.endswith('.jpg' or '.jpeg' or '.png'):
        #select the image
        imgPath = os.path.join(path, infile)
        #get the prediction of the image
        predictions, probabilities = prediction.predictImage(imgPath, result_count=4)
        #Loop the predictions to the terminal
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , str(round(eachProbability,2)), "%")
        #Open the image for modification using PIL
        i = Image.open(os.path.join(path, infile))
        #Save the file name and type as strings
        fn, fext = os.path.splitext(infile)

        #Draw 1st prediction
        draw = ImageDraw.Draw(i)
        #Get string of prediction and probability
        predicted = str(predictions[0])
        probability = str(round(probabilities[0], 2))
        #The text to draw on the picture
        drawtext = predicted + " : " + probability + "%"
        #Border
        draw.text((-1,-1), drawtext,(0,0,0),font=font)
        draw.text((1,1), drawtext,(0,0,0),font=font)
        #Actual text
        draw.text((0, 0), drawtext,(255,255,255),font=font)

        #Draw 2nd prediction
        predicted2 = str(predictions[1])
        probability2 = str(round(probabilities[1], 2))
        drawtext = predicted2 + " : " + probability2 + "%"
        y = 30
        draw.text((-1,y-1), drawtext,(0,0,0),font=font)
        draw.text((1,y+1), drawtext,(0,0,0),font=font)
        draw.text((0, y), drawtext,(255,255,255),font=font)

        #Save the newly edited image in the predicted directory
        i.save('{}/{}/{}{}'.format(savePath, predicted, fn, fext))
