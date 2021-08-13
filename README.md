# WestLotSpot
Working to use object recognition to make Wentworth parking more predictable.

## Description
Currently thers is no easy way for faculty and commuters to check the number of available parking spots in West Lot. The solution proposed is also a clear demonstration of the applications of object recognition and could be used for educational/informational purposes in addition to providing a real solution this problem.

Utilizing a camera which takes photos of the whole lot every few minutes, we calculate the approximate number of parking spots remaining by using YOLO v3 running on an nvidia Jetson to recognize the cars currently in the lot. We can also provide a photo of the lot on the web interface to provide a visual of the number of spots remaining. This aproxomation is then used to update a status on our web interface which indicates weather the lot is nearly full or not. Historical data of the parking capacity at different times throughout the day will be displayed though our webdash for analysis.

## Installation Instructions 

This project was built and tested on a jetson nano however it can be run on any system running ubuntu Linux with python 2.7.
The first and most complicated part of this setup is installing DNN and the Yolo framework. More info on this including example projects as well as installation instructions for all the dependencies can be found at: https://github.com/AlexeyAB/darknet


Next you'll need to download the WestLotSpot repo in your local home/user, once installed some minor tweaks will need to be made to the code in order to locate the appropriate reference files, the structure of the current files refenced in our script is:
<pre>
|-📁home
    |-📁user
        |-📁darknet (darkent install folder containing reference files plus all other dnn related work)
        |  |-📁weights
        |  |  |-coco.weights
        |  |-📁cfg
        |  |  |-yolov3.cfg
        |  |-darknet.py
        |-📁WestLotSpot (this repo)
        |  |-yoloParking.py
 </pre>    
If you look in yoloParking.py you’ll see the references we’re talking about: 
```
imagePath = "/home/munzz11/WestLotSpot/capture.jpg" #Path to image
yolo = "/home/munzz11/darknet" #Path to yolo directory 
```
Change these paths to match your user directory and make sure the structure of your darknet install folder is the same, and you should be all set.

No to start our image recogniton you can simple run the yoloParking.py script using: 
```
sudo python yoloParking.py
```
Next start the webpage, in another terminal run:
```
cd /home/<user>/WestLotSpot/parking_traker_website/
python3 manage.py runserver
```

You should now be able to access the website on localhost:8000

Getting the website and object detection running is the major hurtles, once running the oinly backend access is through the standard django localhost:8000/admin page, which you cna create a user for through the django terminal.
![image](https://user-images.githubusercontent.com/45202950/129286055-f07c8a14-61dd-4d80-b431-35f67db74763.png)
