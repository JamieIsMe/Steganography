# Basic Steganography

Created to allow strings to be placed into images, and to further increase my understanding of Steganography.\
Only accepts **.pngs** due to their compression formating

## Requirements

Uses OpenCV and NumPy

```bash
pip install opencv-python
pip install numpy
```

## Usage
Prompts user to input **1** or **2** based on whether they wish to **encode** or **decode**\
Then prompts user to enter name of the image they wish to **encode**/**decode**


```python
input("1 to encode, 2 to decode: ")

input("Enter image name: ")+'.png'

```
