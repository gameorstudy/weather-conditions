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
#Path to the model That is being used
modelPath = "sampletest/model_ex-122_acc-1.000000.h5"
#Date for naming the directory
today = date.today()
date = today.strftime("%d-%m-%Y")
#String for creating a new directory
savePath = path + "/" + str(date)

#Result counters
totalAccuracy = 0
totalCorrect = 0
totalWrong = 0
totalWrongAccuracy = 0
guessesSunny = 0
guessesRain = 0
guessesCloudy = 0
guessesSnow = 0

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
prediction.setModelPath(modelPath)
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
        print(infile)
        #Open the image for modification using PIL
        i = Image.open(os.path.join(path, infile))
        #Save the file name and type as strings
        fn, fext = os.path.splitext(infile)
        #Draw 1st prediction
        draw = ImageDraw.Draw(i)
        #Get string of prediction and probability
        predicted = str(predictions[0])
        probability = str(round(probabilities[0], 2))
        probabilityInt = int(round(probabilities[0], 2))
        
        #Extra accuracy for results
        correctWeather = "snow"

        if predicted == "snow":
            guessesSnow += 1
        elif predicted == "rain":
            guessesRain += 1
        elif predicted == "sunny":
            guessesSunny += 1
        else:
            guessesCloudy += 1
            
        if predicted == correctWeather:
            totalCorrect += 1
            totalAccuracy += probabilityInt
        else:
            totalWrong +=1
            totalWrongAccuracy += probabilityInt
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
        
finalAccuracy = totalAccuracy / totalCorrect
finalWrongAccuracy = totalWrongAccuracy / totalWrong
totalGuesses = guessesSunny + guessesCloudy +guessesRain + guessesSnow
print("Final accuracy when correct: " + str(finalAccuracy) + "%")
print("Final accuracy when wrong: " + str(finalWrongAccuracy) + "%")
print("Total guesses: " + str(totalGuesses))
print("Sunny guesses: " + str(guessesSunny) + ", Cloudy guesses: " + str(guessesCloudy) +", Rain guesses: " + str(guessesRain) +", Snow guesses: " + str(guessesSnow))