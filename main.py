import cv2
import numpy as np
def binaryConverter(data):
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes):
        return ''.join([format(i, "08b") for i in data])
    elif isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")

def encode_message(picture, data):
    image = cv2.imread(picture)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    index = 0
    data += "!EOF"
    binaryData = binaryConverter(data)
    dataLength = len(binaryData)
    for row in image:
        for pixel in row:
            R, G, B = binaryConverter(pixel)
            for i in range(3):
                current = R if i == 0 else G if i == 1 else B
                if index < dataLength:
                    pixel[i] = int(current[:-1] + binaryData[index], 2)
                    index += 1
                if index >= dataLength:
                    break
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def decode_message(picture):
    image = cv2.imread(picture)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    data = ""
    for row in image:
        for pixel in row:
            R, G, B = binaryConverter(pixel)
            for i in range(3):
                current = R if i == 0 else G if i == 1 else B
                data += current[-1]
    test = [data[i:i+8] for i in range(0, len(data), 8)]
    decodedData = ""
    for i in test:
        decodedData += chr(int(i, 2))
        if decodedData[-4:] == "!EOF":
            break
    return decodedData[:-4]


choice = input("1 to encode, 2 to decode: ")
if choice == "1":
    userMessage = input("Enter a string: ")
    userImage = input("Enter image name: ")+'.png'
    cv2.imwrite("test.png", encode_message(userImage, userMessage))
else:
    encodedImage = input("Enter image to decode: ")+'.png'
    a = decode_message(encodedImage)
    print(a)
