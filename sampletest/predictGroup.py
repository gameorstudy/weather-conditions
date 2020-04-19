from imageai.Prediction.Custom import CustomImagePrediction
import os
import os.path
import datetime
from datetime import date
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
#Picture to open
path = "sampletest/testdata"
today = date.today()
date = today.strftime("%d-%m-%Y")
savePath = path + "/" + str(date)
try:
    os.mkdir(savePath)
    print("Directory ", savePath, " created.")
except FileExistsError:
    print("Directory ", savePath, " already exists.")

count = 1
random.seed(1)
font = ImageFont.truetype("arial.ttf", 26)

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("sampletest/model_ex-110_acc-0.722222.h5")
prediction.setJsonPath("sampletest/model_class.json")
prediction.loadModel(num_objects=10)

for infile in os.listdir(path):
    if infile.endswith('.jpg' or '.jpeg' or '.png'):
        imgPath = os.path.join(path, infile)
        predictions, probabilities = prediction.predictImage(imgPath, result_count=4)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , str(round(eachProbability,2)), "%")
        i = Image.open(os.path.join(path, infile))
        fn, fext = os.path.splitext(infile)
        #Draw 1st prediction
        draw = ImageDraw.Draw(i)
        predicted = str(predictions[0])
        probability = str(round(probabilities[0], 2))
        drawtext = predicted + " : " + probability + "%"
        draw.text((-1,-1), drawtext,(0,0,0),font=font)
        draw.text((1,1), drawtext,(0,0,0),font=font)
        draw.text((0, 0), drawtext,(255,255,255),font=font)
        #Draw 2nd prediction
        predicted2 = str(predictions[1])
        probability2 = str(round(probabilities[1], 2))
        drawtext = predicted2 + " : " + probability2 + "%"
        y = 30
        draw.text((-1,y-1), drawtext,(0,0,0),font=font)
        draw.text((1,y+1), drawtext,(0,0,0),font=font)
        draw.text((0, y), drawtext,(255,255,255),font=font)
        randomValue = random.randint(0, 100000)
        i.save('{}/{}_{}_{}{}'.format(savePath, count, predicted, randomValue, fext))
        count += 1
