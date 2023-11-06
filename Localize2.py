import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import Sampling
# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
# image = Image.open(r"C:\Users\Chris\Desktop\Veysel_s files\noblur.jpg")

#C:\Users\Chris\Desktop\Veysel_s files\noblur.jpg"

def totalBrightness(picture):
    total = 0
    for x in range(0, len(picture)):
        for y in range(0, len(picture[0])):
            total += picture[x, y][2]
    return total



def localize():
    pano = cv2.imread("/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/Panorama.jpeg")
    panorama = cv2.cvtColor(pano, cv2.COLOR_BGR2HSV)
    panorama = cv2.hconcat([panorama, panorama])
    plt.imshow(panorama)
    plt.title('Panorama')
    plt.show()

    panoSamples = []
    for i in range(panorama.shape[1]): # Panorama's width
        panoramaClone = panorama
        panoSamples.append(panoramaClone[0:240, i:i+320])

    panoSampleTotalBrightnesses = []

    for i in range(len(panoSamples)):
        panoSampleTotalBrightnesses.append(totalBrightness(panoSamples[i]))

    picture = cv2.imread("/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/latestImage")
    # normalize(picture)
    # blur(picture)
    origialTotalBrightness = totalBrightness(picture)

    likelihoods = []
    for i in range(len(panoSampleTotalBrightnesses)):
        likelihoods.append(abs(origialTotalBrightness - panoSampleTotalBrightnesses[i]))

    return Sampling.sample(panoSampleTotalBrightnesses, likelihoods)

def blur(picture):
    # Blurring image by sending the ImageFilter.
    # GaussianBlur predefined kernel argument
    picture = picture.filter(ImageFilter.GaussianBlur)
