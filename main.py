import cv2
import numpy as np
def str_to_bin(data):
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes):
        return ''.join([format(i, "08b") for i in data])
    elif isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]

def encode_message(picture, data):
    image = cv2.imread(picture)
    byteAmount = image.shape[0] * image.shape[1] * 3//8
    index = 0
    data += "!EOF"
    binaryData = str_to_bin(data)
    dataLength = len(binaryData)
    if dataLength > byteAmount:
        print("Not enough bytes in the image")
        exit(1)

    for row in image:
        for pixel in row:
            R, G, B = str_to_bin(pixel)
            for i in range(3):
                current = R if i == 0 else G if i == 1 else B
                if index < dataLength:
                    pixel[i] = int(current[:-1] + binaryData[index], 2)
                    index += 1
                if index >= dataLength:
                    break
    return image


userMessage = input("Enter a string")
userImage = input("Enter image name")+'.png'

cv2.imwrite("new.png", encode_message(userImage, userMessage))
