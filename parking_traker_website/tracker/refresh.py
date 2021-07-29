import json

def refresh_image(index):
    url = f'/home/munzz11/WestLotSpot/Output.jpg'
    copy(url)


def get_count(index):
    file = open('/home/munzz11/WestLotSpot/Output.json',)
    data = json.load(file)
    print(data)
    refresh_image(index)
    return data

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