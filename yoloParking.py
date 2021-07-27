import numpy as np
import argparse
import time
import cv2
import os 

imagePath = "/home/munzz11/Pictures/TestLot1/im5.jpg" #Path to image
yolo = "/home/munzz11/darknet" #Path to yolo directory
minConfidence = 0.5 #Minimum probability to filter weak detections
threshold = 0.3 #Threshold when applying non-maxima supression


def detect(imagePath, yolo, minConfidence, threshold):

    #Load input image and grab dimensions 
    image = cv2.imread(imagePath)
    (H, W) = image.shape[:2]

    ln = net.getLayerNames()
    ln = [ln[i[0]-1] for i in net.getUnconnectedOutLayers()]

    #convert to blob, pass image forward through network
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    #timeing info
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    #This section is for vizualizing the output

    boxes = []
    confidences = []
    classIDs = []
    numCars = 0

    #Loop over every output layer
    for output in layerOutputs:
        #loop over each detection in the layer
        for detection in output:
            #grab class ID aka object name and confidence 
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            #remove weak scores and scale boxes back to image scale
            if confidence > minConfidence:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                #find the top left corner of the bounding box
                x = int(centerX - (width/2))
                y = int(centerY - (height /2))
                #update the list with bounding box coords, confidences and calssIDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
                #count the number of cars detected which are of classID 2
                if classID  == 2 or 7 : 
                    numCars = numCars + 1
                


    #Apply Non-maxima suppression to prevent double detection
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, minConfidence, threshold)

    if len(idxs) > 0:
        #loop over each index
        for i in idxs.flatten():
            #grab bounding box coords
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            #draw bounding box amd label
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y+h), color, 2)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    #Save the output image
    cv2.imwrite("Output.jpg", image)

    print("[INFO] Output image saved successfully")

    print("[INFO] %2d cars detected" % (numCars))

def takePhoto(imagePath, yolo):
    camera = cv2.VideoCapture(0)
    # Check success
    if not camera.isOpened():
        raise Exception("[ERROR] Could not open video device")
    # Read picture. ret === True on success
    ret, image = camera.read()
    cv2.imwrite('capture.jpg', image)
    # Close device 
    del(camera)

##SETUP##

#Load the coco class labels
labelsPath =  yolo + "/coco.names"
LABELS = open(labelsPath).read().strip().split("\n")

#Assign a color to each class label for later bounding
np.random.seed(69)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

#Load Weight and Model locations
weightsPath = yolo + "/weights/yolov3.weights"
configPath = yolo + "/cfg/yolov3.cfg"

#Load YOLO object detector trained on coco dataset
print("[INFO] Loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath,weightsPath)

##LOOP##
#while True:

detect(imagePath, yolo, minConfidence, threshold)
takePhoto(imagePath,yolo)
