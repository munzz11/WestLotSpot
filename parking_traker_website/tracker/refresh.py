import json
from random import randrange

def refresh_image(index):
    # url = f'/home/munzz11/WestLotSpot/Output.jpg'
    # copy(url)
    return


def get_count():
    # file = open('/home/munzz11/WestLotSpot/Output.json',)
    # data = json.load(file)
    # print(data)
    # refresh_image(index)
    # return data
    return randrange(11)

def copy(img_url):
    
    image_file = open(img_url,'rb')
    print(image_file)
    file = open('./static/media/parking.jpeg','wb+')
    BUFSIZ = 2048
    image_data = image_file.read(BUFSIZ)


    while image_data:
        #print(i)
        file.write(image_data)
        image_data = image_file.read(BUFSIZ)

    image_file.close()