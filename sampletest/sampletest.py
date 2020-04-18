from imageai.Prediction.Custom import CustomImagePrediction
import os
from PIL import Image
#Picture to open
path = "sampletest/"
picture = "DSC_0182.jpg"
picturePath = path + picture

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("sampletest/model_ex-110_acc-0.722222.h5")
prediction.setJsonPath("sampletest/model_class.json")
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage(picturePath, result_count=4)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
img = Image.open(picturePath)
img.show()