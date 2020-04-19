'''
Predict selected image using the trained model
'''
from imageai.Prediction.Custom import CustomImagePrediction
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#Picture to open
path = "sampletest/"
picture = "DSC_0182.jpg"
picturePath = path + picture
font = ImageFont.truetype("arial.ttf", 108)

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("sampletest/model_ex-110_acc-0.722222.h5")
prediction.setJsonPath("sampletest/model_class.json")
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage(picturePath, result_count=4)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , str(round(eachProbability,2)), "%")
img = Image.open(picturePath)
draw = ImageDraw.Draw(img)
predictied = str(predictions[0])
probability = str(round(probabilities[0], 2))
drawtext = predictied + " : " + probability + "%"
draw.text((0, 0), drawtext,(255,255,255),font=font)
img.save('sample.jpg')
img.show()