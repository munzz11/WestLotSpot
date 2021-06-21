# WestLotSpot
Working to use object recognition to make Wentworth parking more predictable.

## Description
Currently thers is no easy way for faculty and commuters to check the number of available parking spots in West Lot. The solution proposed is also a clear demonstration of the applications of object recognition and could be used for educational/informational purposes in addition to providing a real solution this problem.

Utilizing a camera which takes photos of the whole lot every few minutes, we calculate the approximate number of parking spots remaining by using YOLO v3 running on an nvidia Jetson to recognize the cars currently in the lot. We can also provide a photo of the lot on the web interface to provide a visual of the number of spots remaining. This aproxomation is then used to update a status on our web interface which indicates weather the lot is nearly full or not. Historical data of the parking capacity at different times throughout the day will be displayed though our webdash for analysis.



