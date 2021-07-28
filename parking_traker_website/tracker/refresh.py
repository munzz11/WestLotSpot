def refresh_image(index):
    url = f'./static/media/parking{index}.jpg'
    copy(url)


def get_count(index):
    current = [7, 8, 7, 4, 4, 5, 9, 8, 7, 8]
    refresh_image(index)
    return current[index]

def copy(img_url):
    
    image_file = open(img_url,'rb')
    #print(image_file)
    file = open('./static/media/parking.jpeg','wb+')
    BUFSIZ = 2048
    image_data = image_file.read(BUFSIZ)


    while image_data:
        #print(i)
        file.write(image_data)
        image_data = image_file.read(BUFSIZ)

    image_file.close()